import requests

import google.generativeai as palm


img = 'food3.jpg'
api_user_token = 'e9338e57e3eda54b26a28570397212eb377c32a7'
headers = {'Authorization': 'Bearer ' + api_user_token}

# Single/Several Dishes Detection
url = 'https://api.logmeal.es/v2/image/segmentation/complete'
resp = requests.post(url,files={'image': open(img, 'rb')}, headers=headers)
result = (resp.json()["segmentation_results"]) # display dish only

ingredient_list = []
ingredient_p = ""

for key in result:
    rec_results = key["recognition_results"]
    ingredient = rec_results[0]['name']
    ingredient_list.append(ingredient)
    ingredient_p += ingredient + ", "
    
print("ingredient_list:")
print(ingredient_p + "\n\n")

############# GOOGLE API REQUEST TO GENERATE RECIPIE LIST ###########################
palm.configure(api_key="AIzaSyBorj1JtDM8CCtGwcj21vF7AxU0xVlv6AM")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.95,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "Given a list of ingredients, generate a single detailed quick and easy to cook dish with its recipie that uses only the ingredients provided."
examples = [
  [
    "chicken, lemon, pepper, rice",
    "**Ingredients:**\n* 1 pound boneless, skinless chicken breasts, cut into 1-inch pieces\n* 1/2 teaspoon salt\n* 1/4 teaspoon black pepper\n* 1 tablespoon olive oil\n* 1/2 cup chopped onion\n* 1/2 cup chopped green bell pepper\n* 1 clove garlic, minced\n* 1/4 cup dry white wine\n* 1/4 cup chicken broth\n* 1/4 cup lemon juice\n* 1/4 cup chopped fresh parsley\n* 1 cup cooked rice\n\n**Instructions:**\n1. Season the chicken with salt and pepper.\n2. Heat the olive oil in a large skillet over medium heat.\n3. Add the chicken and cook until browned on all sides, about 5 minutes.\n4. Add the onion, green pepper, and garlic and cook until softened, about 3 minutes.\n5. Add the wine, chicken broth, lemon juice, and parsley. Bring to a boil, then reduce heat and simmer for 10 minutes, or until the chicken is cooked through.\n6. Serve over cooked rice."
  ]
]
messages = []
messages.append(ingredient_p)
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)
print(response.last) # Response of the AI to your most recent request


