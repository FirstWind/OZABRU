# from django.test import TestCase
# from django.contrib.auth import get_user_model
#
#
# class UsersManagersTests(TestCase):
#
#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(email='normal@user.com', password='foo')
#         self.assertEqual(user.email, 'normal@user.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(email='')
#         with self.assertRaises(ValueError):
#             User.objects.create_user(email='', password="foo")
#
#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser('super@user.com', 'foo')
#         self.assertEqual(admin_user.email, 'super@user.com')
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 email='super@user.com', password='foo', is_superuser=False)
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class userProfileTestCase(APITestCase):
    profile_list_url=reverse('all-profiles')
    def setUp(self):
        # создайте нового пользователя, отправив запрос к конечной точке djoser
        self.user_human=self.client.post('/auth/digest/', data={'email':'FirstWind@mail.ru','password':'i-keep-jumping'})
        # получить веб-токен JSON для вновь созданного пользователя
        response=self.client.post('/auth/jwt/create/', data={'email':'FirstWind@mail.ru','password':'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    # получить список всех профилей пользователей во время аутентификации пользователя запроса
    def test_userprofile_list_authenticated(self):
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    # получить список всех профилей пользователей, пока запрос пользователя не прошел проверку подлинности
    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user_human=None)
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    # проверьте, чтобы получить данные профиля аутентифицированного пользователя
    def test_userprofile_detail_retrieve(self):
        response=self.client.get(reverse('profile',kwargs={'pk':1}))
        # print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    # заполнить профиль пользователя, который был автоматически создан с использованием сигналов
    def test_userprofile_profile(self):
        profile_data={'first_name':'Oleg','last_name':'Doroh',}
        response=self.client.put(reverse('profile',kwargs={'pk':1}),data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
