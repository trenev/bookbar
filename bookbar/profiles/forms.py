from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

# UserModel = get_user_model()
#
#
# class ProfileEditForm(auth_forms.UserChangeForm):
#     class Meta:
#         model = UserModel
#         fields = ['email']
#
#         def save(self, commit=True):
#             user = super().save(commit=commit)
#
#             profile = Profile(
#                 user=user,
#             )
#             if commit:
#                 profile.save()
#
#             return user
