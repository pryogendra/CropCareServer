from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from CropCare.settings import EMAIL_HOST_USER
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import base64
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
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
def emailregister(request):
    if request.method=='POST':
        email=request.POST.get('email')
        # email='pryogendra95449@gmail.com'
        text_content ="""Please fill the form given below:
    """
        html_content = render_to_string("emailregister.html")
        try:
            msg = EmailMultiAlternatives(
                "Register",
                text_content,
                settings.EMAIL_HOST_USER,
                [email],
                )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponse("""
            <div
                style="background-color: #28a745;
                color: white; padding: 10px;
                border-radius: 5px;
                text-align: center;">
                Success! Your operation was completed successfully.
            </div>
            """)
            # return JsonResponse(status=status.HTTP_200_OK)
        except:
            return HttpResponse("""
            <div
                style="background-color: #dc3545;
                color: white; padding: 10px;
                border-radius: 5px;
                text-align: center;">
                Error! Something went wrong.
            </div>
            """)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("""
            <div
                style="background-color: #28a745;
                color: white; padding: 10px;
                border-radius: 5px;
                text-align: center;">
                Success! Your registration was completed successfully.
            </div>
            """)
        return HttpResponse("""
        <div
            style="background-color: #dc3545;
            color: white; padding: 10px;
            border-radius: 5px;
            text-align: center;">
            Error! Something went wrong.
        </div>
        """)

@api_view(['POST'])
def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            text_content = """Please fill the form given below:"""
            html_content = render_to_string("forgetpassword.html")
            try:
                msg = EmailMultiAlternatives(
                    "Reset Password",
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                return HttpResponse("""
                    <div style="background-color: #28a745; color: white; padding: 10px; border-radius: 5px; text-align: center;">
                        Success! Your operation was completed successfully.
                    </div>
                    <div style="margin-top: 40px;text-align: center;font-size: 12px;color: #666;">
                        <p><strong>Crop Care Pvt. Ltd.</strong><br>
                           TCSC Campus<br>
                           Kandivali East, Mumbai<br>
                           Email: thecropcare.team@gmail.com<br>
                           Phone: +91 6391348273</p>
                    </div>
                """)
            except Exception as e:
                return HttpResponse(f"""
                    <div style="background-color: #dc3545; color: white; padding: 10px; border-radius: 5px; text-align: center;">
                        Error! Something went wrong: {str(e)}
                    </div>
                    <div style="margin-top: 40px;text-align: center;font-size: 12px;color: #666;">
                        <p><strong>Crop Care Pvt. Ltd.</strong><br>
                           TCSC Campus<br>
                           Kandivali East, Mumbai<br>
                           Email: thecropcare.team@gmail.com<br>
                           Phone: +91 6391348273</p>
                    </div>
                """)
        except User.DoesNotExist:
            send_mail(
                "Alert!",
                "Your email is not registered in the CropCare Pvt. Ltd.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return HttpResponse("""
                <div style="background-color: #dc3545; color: white; padding: 10px; border-radius: 5px; text-align: center;">
                    Error! Your email is not registered in our system.
                </div>
                <div style="margin-top: 40px;text-align: center;font-size: 12px;color: #666;">
                    <p><strong>Crop Care Pvt. Ltd.</strong><br>
                       TCSC Campus<br>
                       Kandivali East, Mumbai<br>
                       Email: thecropcare.team@gmail.com<br>
                       Phone: +91 6391348273</p>
                </div>
            """)
    else:
        return HttpResponse("""
        <div
            style="background-color: #dc3545;
            color: white; padding: 10px;
            border-radius: 5px;
            text-align: center;">
            Error! Something went wrong.
        </div>
        <div style="margin-top: 40px;text-align: center;font-size: 12px;color: #666;">
            <p><strong>Crop Care Pvt. Ltd.</strong><br>
               TCSC Campus<br>
               Kandivali East, Mumbai<br>
               Email: thecropcare.team@gmail.com<br>
               Phone: +91 6391348273</p>
        </div>
        """)

@api_view(['POST'])
def newPassword(request):
    if request.method=='POST':
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        email=request.POST.get('email')
        if pass1==pass2:
            user = User.objects.get(email=email)
            user.set_password(pass1)
            user.save()
            return HttpResponse("""
            <div
                style="background-color: #28a745;
                color: white; padding: 10px;
                border-radius: 5px;
                text-align: center;">
                Success! Your operation was completed successfully.
            </div>
            """)
        else:
            return HttpResponse("""
            <div
                style="background-color: #dc3545;
                color: white; padding: 10px;
                border-radius: 5px;
                text-align: center;">
                Error! Password are not matched.
            </div>
            """)
    else:
        return HttpResponse("""
        <div
            style="background-color: #dc3545;
            color: white; padding: 10px;
            border-radius: 5px;
            text-align: center;">
            Error! Something went wrong.
        </div>
        <div style="margin-top: 40px;text-align: center;font-size: 12px;color: #666;">
            <p><strong>Crop Care Pvt. Ltd.</strong><br>
               TCSC Campus<br>
               Kandivali East, Mumbai<br>
               Email: thecropcare.team@gmail.com<br>
               Phone: +91 6391348273</p>
        </div>
        """)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return JsonResponse({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post(request):
    if request.method=='POST':
        data=[]
        CURRENT_USER = request.POST.get('CURRENT_USER')
        user=User.objects.get(username=CURRENT_USER)
        obj=UserProfile.objects.get(user=user)
        posts = Post.objects.all()
        for post in posts:
            p={
            'post_id':post.id,
            'username':post.user.user.username, # posted user
            'avtar':image_to_base64(post.user.profile_image.path) if post.user.profile_image else None, # posted user profile
            'profile_pic':image_to_base64(obj.profile_image.path) if obj.profile_image else None, # user profile
            'data':image_to_base64(post.image.path) if post.image else None,
            'data_type':post.data_type,
            'caption':post.caption,
            'likes':post.likes,
            'comments':post.comments,
            'posted_ago':post.posted_ago,
            }
            data.append(p)
        return JsonResponse({'data':data},status=status.HTTP_200_OK)

@api_view(['POST'])
def profile(request):
    if request.method=='POST':
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
        return JsonResponse({'data':data},status=status.HTTP_200_OK)

@api_view(['POST'])
def updateprofile(request):
    try :
        if request.method=='POST':
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

@api_view(['POST'])
def schemes(request):
    if request.method=='POST':
        data=[]
        obj=Govt_Scheme.objects.all()
        for sch in obj:
            data.append(sch.title)

        return JsonResponse({'data':data},status=status.HTTP_200_OK)

@api_view(['POST'])
def schemedetail(request):
    if request.method=='POST':
        id=request.POST.get('id')
        obj=Govt_Scheme.objects.filter(id=id).first()
        print("Govt : ",obj)
        if obj is None:
            print("Govt_Scheme not found")
        else:
            data={
            'title':obj.title,
            'discription':obj.discription,
            'benefit':obj.benefit,
            'eligibility':obj.eligibility,
            'document':obj.document,
            'apply_process':obj.apply_process,
            'contact':obj.contact,
            }

            return JsonResponse({'data':data},status=status.HTTP_200_OK)

@api_view(['POST'])
def shopping(request):
    if request.method=='POST':
        data=[]
        prods=Shopping.objects.all().order_by('type')
        for prod in prods:
            p={
            'product_id':prod.id,
            'type':prod.type,
            'title':prod.title,
            'image':image_to_base64(prod.image.path) if prod.image else None,
            'info1':prod.info1,
            'info2':prod.info2,
            }
            data.append(p)
        #return HttpResponse("shopping")
        return JsonResponse({'data':data},status=status.HTTP_200_OK)

@api_view(['POST'])
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        contact=ContactUs(name=name, email=email, message=message)
        contact.save()
        return JsonResponse({'message':'sucess'},status=status.HTTP_200_OK)

@api_view(['POST'])
def feedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        message=request.POST.get('message')

        feed=FeedBack(name=name, message=message)
        feed.save()

        return JsonResponse({'message':'sucess'}, status=status.HTTP_200_OK)

def add_scheme(request):
    schemes = {
            "Gramin Bhandaran Yojana": {
                "Description": "Promotes the construction of storage facilities for farmers.",
                "Benefits": "Financial support for building warehouses.",
                "Eligibility": "Farmers, NGOs, cooperatives.",
                "Documents": "Project proposal, Aadhaar, land records.",
                "How to Apply": "Apply through nabard.org or district agriculture offices.",
                "Contact": "1800-123-1551"
            }
        }
    for i in schemes.keys():
        govt=Govt_Scheme(
            title=i,
            discription=schemes[i]['Description'],
            benefit=schemes[i]['Benefits'],
            eligibility=schemes[i]['Eligibility'],
            document=schemes[i]['Documents'],
            apply_process=schemes[i]['How to Apply'],
            contact=schemes[i]['Contact'],
        )
        govt.save()

        # print(i,schemes[i]['Description'],schemes[i]['Benefits'],
        # schemes[i]['Eligibility'],schemes[i]['Documents'],
        # schemes[i]['How to Apply'],schemes[i]['Contact'],)
    return HttpResponse("scheme")

@csrf_exempt
def emailregister(request):
    # text_content = render_to_string("email.txt",context={"my_variable": 42},)
    email=request.POST.get("email")
    url=request.POST.get('url')
    text_content ="""To complete the registeration process, please fill the form given below:
"""


    html_content = render_to_string("emailregister.html",{'url':url})

    msg = EmailMultiAlternatives(
        "!! Welcome !!",
        text_content,
        settings.EMAIL_HOST_USER,
        [email],
        # headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
)

    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("Success")

@csrf_exempt
def sent(request):
    print("Hello...")
    if request.method=='POST':
        email=request.POST.get('email')
        print(email)
        return HttpResponse("{{email}}")
    else:
        return HttpResponse("Failed")

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
