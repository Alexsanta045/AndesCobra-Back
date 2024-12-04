from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import PasswordChangeRequest 
from django.utils import timezone


User = get_user_model()

@csrf_exempt
@require_http_methods(["POST"])
def change_user_password(request):
    try:
        data = json.loads(request.body)
        username_or_email = data.get('username') or data.get('email')
        new_password = data.get('new_password')

        if not username_or_email:
            return JsonResponse({
                'error': 'Se requiere username/email'
            }, status=400)

        # Verificar si el usuario existe
        user = User.objects.filter(username=username_or_email).first() or User.objects.filter(email=username_or_email).first()

        if not user:
            # Si el usuario no existe, no se debe crear una solicitud.
            return JsonResponse({
                'error': 'Usuario no encontrado'
            }, status=404)

        # Validar si ya existe una solicitud de cambio
        existing_request = PasswordChangeRequest.objects.filter(email_or_username=username_or_email, is_changed=False).first()

        if not existing_request:
            # Registrar la solicitud si no existe
            PasswordChangeRequest.objects.create(email_or_username=username_or_email)

        # Si no hay nueva contraseña, es solo una solicitud sin cambio de contraseña
        if not new_password:
            return JsonResponse({
                'message': f'Solicitud de cambio de contraseña registrada para: {username_or_email}'
            }, status=200)

        # Si hay nueva contraseña, cambiarla
        user.set_password(new_password)
        user.save()

        # Marcar la solicitud como procesada
        if existing_request:
            existing_request.is_changed = True
            existing_request.changed_at = timezone.now()  # Establecer la fecha de cambio
            existing_request.save()

        return JsonResponse({
            'message': f'Contraseña cambiada exitosamente para {user.username}'
        }, status=200)

    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Formato JSON inválido'
        }, status=400)

    except Exception as e:
        return JsonResponse({
            'error': f'Error al cambiar la contraseña: {str(e)}'
        }, status=500)


def get_password_change_requests(request):
    try:
        # Obtener todas las solicitudes de cambio de contraseña pendientes
        requests = PasswordChangeRequest.objects.filter(is_changed=False).values('email_or_username', 'created_at', 'is_changed')

        # Convertir las solicitudes a una lista de diccionarios
        requests_list = list(requests)

        return JsonResponse({'requests': requests_list}, status=200)

    except Exception as e:
        return JsonResponse({'error': f'Error al obtener las solicitudes: {str(e)}'}, status=500)

    
    
@csrf_exempt
@require_http_methods(["DELETE"])
def reject_password_change_request(request, username_or_email):
    try:
        # Buscar la solicitud pendiente por usuario o email
        request_to_reject = PasswordChangeRequest.objects.filter(
            email_or_username=username_or_email, 
            is_changed=False, 
            is_rejected=False
        ).first()

        if not request_to_reject:
            return JsonResponse({
                'error': 'No hay una solicitud pendiente o ya fue procesada/rechazada'
            }, status=404)

        # Eliminar la solicitud de la base de datos
        request_to_reject.delete()

        return JsonResponse({
            'message': f'Solicitud de cambio de contraseña para {username_or_email} rechazada y eliminada.'
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'error': f'Error al rechazar la solicitud: {str(e)}'
        }, status=500)
    

def approve_password_change(request, username_or_email):
    try:
        # Buscar el usuario por username o email
        user = User.objects.filter(username=username_or_email).first() or User.objects.filter(email=username_or_email).first()

        if not user:
            return JsonResponse({
                'error': 'Usuario no encontrado. No se puede aprobar la solicitud.'
            }, status=404)

        # Verificar si la solicitud de cambio de contraseña existe
        existing_request = PasswordChangeRequest.objects.filter(email_or_username=username_or_email, is_changed=False).first()

        if not existing_request:
            return JsonResponse({
                'error': 'No hay solicitud pendiente o ya se ha procesado.'
            }, status=404)

        # Cambiar la contraseña
        new_password = request.data.get('new_password')
        if not new_password:
            return JsonResponse({
                'error': 'Se requiere una nueva contraseña.'
            }, status=400)

        user.set_password(new_password)
        user.save()

        # Marcar la solicitud como procesada
        existing_request.is_changed = True
        existing_request.save()

        return JsonResponse({
            'message': f'Contraseña cambiada exitosamente para {user.username}'
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'error': f'Error al procesar la solicitud: {str(e)}'
        }, status=500)
    

def get_password_change_history(request):
    try:
        # Obtener todas las solicitudes con contraseña cambiada
        history = PasswordChangeRequest.objects.filter(is_changed=True).values('email_or_username', 'changed_at')

        # Convertir a lista
        history_list = list(history)

        return JsonResponse({'history': history_list}, status=200)
    except Exception as e:
        return JsonResponse({'error': f'Error al obtener el historial: {str(e)}'}, status=500)

