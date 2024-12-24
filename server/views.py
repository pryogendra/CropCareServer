from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import UserProfile,Post
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import base64
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.contrib.auth.models import User


def image_to_base64(urlPath):
    with open(urlPath, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return image_data

def base64_to_image(image_base64,format="JPEG"):
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))
    image_io = BytesIO()
    image.save(image_io, format=format)
    image_io.seek(0)
    return image_io

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post(request):
    data=[]
    posts = Post.objects.all()
    # print(f"Current User : {posts[1].user}")
    #profile=UserProfile.objects.filter(user=posts.user)
    for post in posts:
        p={
        'post_id':post.id,
        'username':post.user.user.username,
        'avtar':post.user.profile_image.url if post.user.profile_image else None,
        'profile_pic':post.user.profile_image.url if post.user.profile_image else None,
        'data':post.image.url if post.image else None,
        'image':post.user.profile_image.url if post.user.profile_image else None,
        'caption':post.caption,
        'likes':post.likes,
        'comments':post.comments,
        'posted_ago':post.posted_ago,
        }
        data.append(p)
    # print(data)
    #return HttpResponse("Posts")
    return JsonResponse({'data':data},status=status.HTTP_200_OK)

@csrf_exempt
def profile(request):
    CURRENT_USER = request.POST.get('CURRENT_USER')
    user=User.objects.get(username=CURRENT_USER)
    obj=UserProfile.objects.get(user=user)
    data={
        'username':obj.user.username,
        'email':user.email,
        'mobile':obj.mobile,
        'location':obj.location,
        'pincode':obj.pincode,
        'profile_image': image_to_base64(obj.profile_image.path) if obj.profile_image else None,
    }
    # print(data)
    return JsonResponse({'data':data},status=status.HTTP_200_OK)

@api_view(['POST'])
def updateprofile(request):
    try :
        CURRENT_USER = request.POST.get('CURRENT_USER')
        file_name=f'{CURRENT_USER}_profile.jpg'
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        location=request.POST.get('location')
        pincode=request.POST.get('pincode')
        image_base64=request.POST.get('profile_image')
        user=User.objects.get(username=CURRENT_USER)
        obj=UserProfile.objects.get(user=user)
        if image_base64 is not None :
            image_io=base64_to_image(image_base64)
            obj.profile_image.save(file_name, ContentFile(image_io.read()), save=True)
        if email:
            user.email=email
            user.save()
        if mobile:
            obj.mobile=mobile
        if location:
            obj.location=location
        if pincode:
            obj.pincode=pincode
        obj.save()
        return JsonResponse({'message': 'Profile Updated successfully','status':'!! Success !!'})
    except Exception as e :
        return JsonResponse({'message': f'{e} : Profile not Updated.','status':'!! Error !!'})

# @api_view(['POST']) # demo VIEW
# def upload_image(request):
#     if request.method == 'POST':
#         try:
#             image_base64 = request.POST.get('image')
#             file_name=request.POST.get('file_name')
#
#             image_data = base64.b64decode(image_base64)
#             image = Image.open(BytesIO(image_data))
#             user = UserProfile.objects.get(id=1)
#             image_io = BytesIO()
#             image.save(image_io, format='JPEG')
#             image_io.seek(0)
#
#             user.profile_image.save(file_name, ContentFile(image_io.read()), save=True)
#             print("Image saved successfully:", user.profile_image)
#             return JsonResponse({'status': 'success'})
#
#         except Exception as e:
#             print("ERROR............................",e)
#             return JsonResponse({'status': 'error', 'message': str(e)})
#
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
#
# @csrf_exempt # demo VIEW
# def get_image(request):
#     try:
#         user = User.objects.get(username='yogi')
#         image_obj = UserProfile.objects.get(user=user)
#         with open(image_obj.profile_image.path, 'rb') as image_file:
#             image_data = base64.b64encode(image_file.read()).decode('utf-8')
#         return JsonResponse({'status': 'success', 'image': image_data})
#     except UserProfile.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Image not found.'}, status=404)
#     except Exception as e:
#         print("Error : ",e)
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
