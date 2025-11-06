from django.shortcuts import render

# Create your views here.


def index_view(request):
	context = {}
	return render(request, "web/index.html", context)

def report_incident_view(request):
	context = {}
	return render(request, "web/report_incident.html", context)

def incidents_view(request):
	context = {}
	return render(request, "web/incidents.html", context)

def neighborhood_watch_view(request):
	context = {}
	return render(request, "web/neighborhood_watch.html", context)

def safety_tips_view(request):
	context = {}
	return render(request, "web/safety_tips.html", context)


def emergency_services_view(request):
	context = {}
	return render(request, "web/emergency_services.html", context)

def how_it_works_view(request):
	context = {}
	return render(request, "web/how_it_works.html", context)


def about_us_view(request):
	context = {}
	return render(request, "web/about_us.html", context)

def faqs_view(request):
	context = {}
	return render(request, "web/faqs.html", context)

def profile_view(request):
	context = {}
	return render(request, "web/profile.html", context)



