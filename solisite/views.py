from django.shortcuts import render, redirect

def landingpage_view(request):
    context = {
        'authenticated': request.user.is_authenticated,
    }
    return render(request, 'solisite/landingpage.html', context)

def about_view(request):
	context = {
        'authenticated': request.user.is_authenticated,
	}
	return render(request, 'solisite/about.html', context)

def imprint_view(request):
	context = {
        'authenticated': request.user.is_authenticated,
	}
	return render(request, 'solisite/imprint.html', context)

def privacy_policy_view(request):
	context = {
        'authenticated': request.user.is_authenticated,
	}
	return render(request, 'solisite/privacy_policy.html', context)

def blog_view(request):
    context = {
        'authenticated': request.user.is_authenticated,
    }
    return render(request, 'solisite/blog.html', context)
