from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si l'utilisateur est déjà authentifié, on ne fait rien
        if hasattr(request, 'user') and request.user.is_authenticated:
            return self.get_response(request)

        # Récupérer le token JWT depuis les en-têtes
        auth_header = request.headers.get('Authorization', '').split()
        
        if len(auth_header) == 2 and auth_header[0] == 'Bearer':
            token = auth_header[1]
            try:
                # Valider le token et récupérer l'utilisateur
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(token)
                user = jwt_auth.get_user(validated_token)
                
                # Authentifier l'utilisateur dans la requête
                request.user = user
                request.auth = validated_token
                
            except (InvalidToken, TokenError) as e:
                # En cas d'erreur de token, on laisse la requête continuer
                # car d'autres middlewares pourraient gérer l'authentification
                pass

        return self.get_response(request)
