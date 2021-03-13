import markovify

# Get raw text as string.
with open("poetry.txt", encoding="utf-8") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)
model_json = text_model.to_json()
# In theory, here you'd save the JSON to disk, and then read it back later.

reconstituted_model = markovify.Text.from_json(model_json)
reconstituted_model.make_short_sentence(140)

# Print five randomly-generated sentences
for i in range(5):
    print(reconstituted_model.make_sentence_with_start("star"))
