from django.shortcuts import render
from django.http import HttpRequest, request
from predictor_app import predictor

# Create your views here.
#hours,practice, teamwork, midterm, finalexam, scores

def predictor_view(request):
    if request.method == "POST":
         hours = float(request.POST.get('hours'))
         practice = float(request.POST.get('practice'))
         teamwork = float(request.POST.get('teamwork'))
         midterm = int(request.POST.get('midterm'))
         final_exam = float(request.POST.get('final_exam'))
         scores = int(request.POST.get('scores'))
         
         grade_result = predictor.predictor(hours, practice, teamwork, midterm, final_exam, scores)

         context = {
              'grade' : grade_result,
              'hours' : hours,
              'practice' : practice,
              'teamwork' : teamwork,
              'midterm': midterm,
              'final_exam': final_exam,
              'scores': scores,

         }

         return render(request, 'index.html', context)
    return render(request, 'index.html')

