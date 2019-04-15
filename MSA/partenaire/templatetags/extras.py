from django import template

register = template.Library()

@register.filter
def partcolor(titre):
     color = '#e0e0e0' 
     if titre == '1' : color = '#e699d4'
     if titre == '2'  : color = '#9eb1d0'

     return color

@register.filter
def partlogo(titre):
     logo = 'logo/Societe.png' 
     if titre == '1' : logo = 'logo/Madame.png' 
     if titre == '2'  : logo = 'logo/Monsieur.png' 

     return logo