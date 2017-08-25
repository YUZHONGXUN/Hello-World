import facebook
token = "EAACEdEose0cBAA1uqrVViIZBo7MgZACcIyJZCe9qDHZBYlSYcZAjq74oLwp1s4ZBypLwKfN8U7UZCZAU5IQFETZBRR23BwES3Imk1xAoYBdm9ZCz2UX0WZA6yXjTEczpZAs2CKpkfhS8mZA366cFvwdZA737l2EHZAQZAzZBOyAiHCQeRg0PsRMCBT8SpfvkxGxZBoH7CuzxgZD"
graph = facebook.GraphAPI(access_token = token)
graph.put_object("me", "feed", message = "I use python to post the facebook article. It's test.")           # me 中心與 feed 另一個點