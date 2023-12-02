from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, path
from django.views import View
from chats.forms import MessageForm
from users.models import CustomUser
from chats.models import Messages
from datetime import datetime


class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        users = CustomUser.objects.all()
        dict_count ={}
        for i in users:
            if i == request.user:
                pass
            else:
                message = Messages.objects.filter(
                    Q(Q(sender=request.user) & Q(recipient=i)) |
                    Q(Q(sender=i) & Q(recipient=request.user))
                )
                count = message.filter(
                    Q(send_status='sending') & Q(sender=i) & Q(recipient=request.user)
                ).count()
                dict_count[i] = count
        context = {
            'dict_count': dict_count,
            'users': users,
        }
        return render(request, 'home.html', context)



class UserDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        messages_form = MessageForm()
        user = CustomUser.objects.get(id=id)
        message = Messages.objects.filter(
            Q(Q(sender=request.user) & Q(recipient=user)) |
            Q(Q(sender=user) & Q(recipient=request.user))
        )
        message = message.order_by('created_time')
        count = message.filter(send_status='sending').count()
        for i in message:
            if i.sender != request.user and i.send_status == 'sending':
                i.send_status = 'sended'
                i.save()

        context = {
            'count': count,
            'user': user,
            'message': message,
            'messages_form': messages_form,
        }
        return render(request, 'contact.html', context)



class MessageView(LoginRequiredMixin, View):
    def post(self, request, id):
        user = CustomUser.objects.get(id=id)
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            Messages.objects.create(
                text=message_form.cleaned_data['text'],
                sender=request.user,
                recipient=user,
                send_status='sending'
            )
            return redirect(reverse('contact', kwargs={'id': user.id}))
        else:
            context = {
                'message_form': message_form,
            }
            return render(request, 'contact.html', context)























































