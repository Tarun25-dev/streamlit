# Confidence Score: How sure the model about its prediction.
# Usually its number between 0 to 1 (like 0% to 100%).
# suppose your model predicts prediction[[0.87]]
# which means 87% confidence about that prediction would be true
# confidence = prediction[0][0]*100
# suppose model output is [[0.87]] why we take [0][0] beacuse the model output shape is 2d array [[0.87]] refers to first row[0] and in that first row thats the first value [0]
# here [0][0] = [0.87]
# 0.87*100 = 87 so the model confidence is 87
# we know that output ranges from 0 to 1 and 0.5 is a threshold value
# usually prediction > 0.5 --> True
# prediction < 0.5 --> False
# {confidence:.2f} → Show 2 decimal places


"""
prediction = model.predict(img_array)
confidence = np.max(prediction) * 100

st.write("Confidence:", f"{confidence:.2f}%")

"""