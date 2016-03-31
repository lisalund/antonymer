from django import forms
#from django.utils.safestring import mark_safe


## src: https://wikis.utexas.edu/display/~bm6432/Django-Modifying+RadioSelect+Widget+to+have+horizontal+buttons
#class HorizRadioRenderer(forms.RadioSelect.renderer):
#    """ this overrides widget method to put radio buttons horizontally
#        instead of vertically.
#    """
#    def render(self):
#            """Outputs radios"""
#            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

#class ApprovalForm(forms.Form):
#	approval = forms.ChoiceField(choices=CHOICES, 
#    	initial=0,
#        widget=forms.RadioSelect(),
#        )

class SomeForm(forms.Form):
		CHOICES = ((1,'1'),
	           (2,'2'),
	           (3,'3'),
	           (4,'4'),
	           (5,'5'),
	           )
		picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect())



