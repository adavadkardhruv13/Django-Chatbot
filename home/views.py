from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI

def chat(request):
    return render(request, 'index.html')

def chatApi(request):
    api_key = "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"

    client = OpenAI(api_key=api_key)

    if request.method == "POST":
        try:
            prompt = request.POST['prompt']
            #messages = [
              #  {"role": "system", "content": "You are a helpful assistant."},
              #  {"role": "user", "content": prompt}
            #]
            response = client.completions.create(
                model="text-davinci-003",  # Specify the model
                prompt=prompt,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return JsonResponse({"output": response["choices"][0]["text"]})

        except Exception as e:
            return JsonResponse({"error": f"Error processing request: {str(e)}"}, status=500)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=400)
