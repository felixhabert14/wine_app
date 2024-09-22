# def ocr_practise(images):
#     image = images[0]
#     # resized = image.resize((1000,1000))
#     # opencv_image = np.array(resized)
#     # gray = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2GRAY)
#     # _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     # img_ar = np.array(binary_image)
#     contours,_ = cv2.findContours(image, 3, 2)
#     cnt_area = []
#     print(len(contours))
#     for i in range(0,len(contours)):
#         cnt_area.append(cv2.contourArea(contours[i]))
#     low_threshold = 20
#     up_threshold = 1000
#     print("Without filters:", len(contours))
#     contours = [cnt for cnt in contours if cv2.contourArea(cnt) > low_threshold \
#                          and cv2.contourArea(cnt) < up_threshold]

#     filtered_contours = sort_contours(contours, method="left-to-right")[0]
#     print("Number of contours:", len(filtered_contours))
    
#     text = ""
#     min_contours = min(len(filtered_contours), 30)
#     assembled_contours = []
#     for i in range(2, min_contours-2, 3):
#         past = filtered_contours[i-1]
#         pres = filtered_contours[i]
#         new = filtered_contours[i+1]
#         x,y,w,h = cv2.boundingRect(past)
#         _,_,w1,_ = cv2.boundingRect(pres)
#         _,_,w2,_ = cv2.boundingRect(new)
#         assembled_contours.append([x, y, x+w+w1+w2, y+h])

#     if len(assembled_contours) != 0:
#         # for item in assembled_contours:

#         for i in range(1,len(assembled_contours),1):
#             cnt = assembled_contours[i]
#             print(cnt)
#             x,y,w,h = cnt
#             x_left = x+w
#             x_right = x
#             dis = x_right-x_left
#             # if dis > -100:
#             #     get_text = translate(x,y,w,h,img_ar)
#             #     if not get_text.isdigit():
#             #         text += get_text
#                 # plt.imshow(let_resized, cmap="gray")
#                 # plt.show())
#             image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,0),1)            
#         _ = plt.figure(figsize=(30, 30))
#         plt.imshow(image, cmap="gray")
#         plt.show()
#     pass



# ocr_practise(images)
# translate(images)
# img.show()
# ocr_practise()
# get_from_file()

# let_img = Image.open("./test_hand.jpg")
# let_img = Image.open("./phrase.png")
# let_img = let_img.resize((800, 300))
# width, height = let_img.size
# im_array  = let_img.resize((width*5, height*5))
# conv = np.array(im_array.convert("RGB"))
# sharpening_filter  = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
# im = cv2.filter2D(conv, -1, sharpening_filter)
# # let_resized = let_img.resize((1000,1000))
# let_img = Image.fromarray(im)


# processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
# model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
# pixel_values = processor(images=let_img, return_tensors="pt").pixel_values
# generated_ids = model.generate(pixel_values)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
# print(generated_text[0])

# def sobel():
    # sobelx = cv2.Sobel(img_ar,cv2.CV_64F,1,0,ksize=5)
    # sobely = cv2.Sobel(img_ar,cv2.CV_64F,0,1,ksize=5)
    # gradient_magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))
    # contours,hierarchy = cv2.findContours(binary_image, 1, 2)
    # # src_gray = cv2.cvtColor(img_ar, cv2.COLOR_BGR2GRAY)
    # threshold = 100
    # canny_output = cv2.Canny(img_ar, threshold, threshold * 2)
    # gradient_direction = np.arctan2(sobely, sobelx)
    # plt.imshow(canny_output)
    # plt.imshow(gradient_magnitude)
    # plt.show()
    # pass


# get_crop_image()


# print(len(contours))
# img = cv2.imread("./latin1.jpg")
# 
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
# dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
#                                                  cv2.CHAIN_APPROX_NONE)
# im2 = img.copy()
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     # Drawing a rectangle on copied image
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

# window_name = 'image'
# cv2.imshow(window_name, im2)
# cv2.waitKey(0)
 # file = open("recognized.txt", "w+")
# file.write("")
# file.close()
 
# # Looping through the identified contours
# # Then rectangular part is cropped and passed on
# # to pytesseract for extracting text from it
# # Extracted text is then written into the text file
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
     
#     # Drawing a rectangle on copied image
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
#     # Cropping the text block for giving input to OCR
#     cropped = im2[y:y + h, x:x + w]
     
#     # Open the file in append mode
#     file = open("recognized.txt", "a")
     
#     # Apply OCR on the cropped image
#     text = pytesseract.image_to_string(cropped)
     
#     # Appending the text into file
#     file.write(text)
#     file.write("\n")
     
#     # Close the file
#     file.close