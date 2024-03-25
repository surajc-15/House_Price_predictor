from flask import Flask, render_template, request
import pickle 
import pandas as pd

model=pickle.load(open('xgboost.pkl','rb'))

dataset={'1st Block Jayanagar': 0,
  '1st Block Koramangala': 1,
  '1st Phase JP Nagar': 2,
  '2nd Phase Judicial Layout': 3,
  '2nd Stage Nagarbhavi': 4,
  '5th Block Hbr Layout': 5,
  '5th Phase JP Nagar': 6,
  '6th Phase JP Nagar': 7,
  '7th Phase JP Nagar': 8,
  '8th Phase JP Nagar': 9,
  '9th Phase JP Nagar': 10,
  'AECS Layout': 11,
  'Abbigere': 12,
  'Akshaya Nagar': 13,
  'Ambalipura': 14,
  'Ambedkar Nagar': 15,
  'Amruthahalli': 16,
  'Anandapura': 17,
  'Ananth Nagar': 18,
  'Anekal': 19,
  'Anjanapura': 20,
  'Ardendale': 21,
  'Arekere': 22,
  'Attibele': 23,
  'BEML Layout': 24,
  'BTM 1st Stage': 25,
  'BTM 2nd Stage': 26,
  'BTM Layout': 27,
  'Babusapalaya': 28,
  'Badavala Nagar': 29,
  'Balagere': 30,
  'Banashankari': 31,
  'Banashankari Stage II': 32,
  'Banashankari Stage III': 33,
  'Banashankari Stage V': 34,
  'Banashankari Stage VI': 35,
  'Banaswadi': 36,
  'Banjara Layout': 37,
  'Bannerghatta': 38,
  'Bannerghatta Road': 39,
  'Basapura': 40,
  'Basavangudi': 41,
  'Basaveshwara Nagar': 42,
  'Battarahalli': 43,
  'Begur': 44,
  'Begur Road': 45,
  'Bellandur': 46,
  'Benson Town': 47,
  'Bharathi Nagar': 48,
  'Bhoganhalli': 49,
  'Billekahalli': 50,
  'Binny Pete': 51,
  'Bisuvanahalli': 52,
  'Bommanahalli': 53,
  'Bommasandra': 54,
  'Bommasandra Industrial Area': 55,
  'Bommenahalli': 56,
  'Brookefield': 57,
  'Budigere': 58,
  'CV Raman Nagar': 59,
  'Chamrajpet': 60,
  'Chandapura': 61,
  'Channasandra': 62,
  'Chikka Tirupathi': 63,
  'Chikkabanavar': 64,
  'Chikkalasandra': 65,
  'Choodasandra': 66,
  'Cooke Town': 67,
  'Cox Town': 68,
  'Cunningham Road': 69,
  'Dairy Circle': 70,
  'Dasanapura': 71,
  'Dasarahalli': 72,
  'Devanahalli': 73,
  'Devarachikkanahalli': 74,
  'Dodda Nekkundi': 75,
  'Doddaballapur': 76,
  'Doddakallasandra': 77,
  'Doddathoguru': 78,
  'Dodsworth Layout': 79,
  'Domlur': 80,
  'Dommasandra': 81,
  'EPIP Zone': 82,
  'Electronic City': 83,
  'Electronic City Phase II': 84,
  'Electronics City Phase 1': 85,
  'Frazer Town': 86,
  'GM Palaya': 87,
  'Ganga Nagar': 88,
  'Garudachar Palya': 89,
  'Giri Nagar': 90,
  'Gollarapalya Hosahalli': 91,
  'Gottigere': 92,
  'Green Glen Layout': 93,
  'Gubbalala': 94,
  'Gunjur': 95,
  'Gunjur Palya': 96,
  'HAL 2nd Stage': 97,
  'HBR Layout': 98,
  'HRBR Layout': 99,
  'HSR Layout': 100,
  'Haralur Road': 101,
  'Harlur': 102,
  'Hebbal': 103,
  'Hebbal Kempapura': 104,
  'Hegde Nagar': 105,
  'Hennur': 106,
  'Hennur Road': 107,
  'Hoodi': 108,
  'Horamavu Agara': 109,
  'Horamavu Banaswadi': 110,
  'Hormavu': 111,
  'Hosa Road': 112,
  'Hosakerehalli': 113,
  'Hoskote': 114,
  'Hosur Road': 115,
  'Hulimavu': 116,
  'ISRO Layout': 117,
  'ITPL': 118,
  'Iblur Village': 119,
  'Indira Nagar': 120,
  'JP Nagar': 121,
  'Jakkur': 122,
  'Jalahalli': 123,
  'Jalahalli East': 124,
  'Jigani': 125,
  'Judicial Layout': 126,
  'KR Puram': 127,
  'Kadubeesanahalli': 128,
  'Kadugodi': 129,
  'Kaggadasapura': 130,
  'Kaggalipura': 131,
  'Kaikondrahalli': 132,
  'Kalena Agrahara': 133,
  'Kalkere': 134,
  'Kalyan nagar': 135,
  'Kambipura': 136,
  'Kammanahalli': 137,
  'Kammasandra': 138,
  'Kanakapura': 139,
  'Kanakpura Road': 140,
  'Kannamangala': 141,
  'Karuna Nagar': 142,
  'Kasavanhalli': 143,
  'Kasturi Nagar': 144,
  'Kathriguppe': 145,
  'Kaval Byrasandra': 146,
  'Kenchenahalli': 147,
  'Kengeri': 148,
  'Kengeri Satellite Town': 149,
  'Kereguddadahalli': 150,
  'Kodichikkanahalli': 151,
  'Kodigehaali': 152,
  'Kodigehalli': 153,
  'Kodihalli': 154,
  'Kogilu': 155,
  'Konanakunte': 156,
  'Koramangala': 157,
  'Kothannur': 158,
  'Kothanur': 159,
  'Kudlu': 160,
  'Kudlu Gate': 161,
  'Kumaraswami Layout': 162,
  'Kundalahalli': 163,
  'LB Shastri Nagar': 164,
  'Laggere': 165,
  'Lakshminarayana Pura': 166,
  'Lingadheeranahalli': 167,
  'Magadi Road': 168,
  'Mahadevpura': 169,
  'Mahalakshmi Layout': 170,
  'Mallasandra': 171,
  'Malleshpalya': 172,
  'Malleshwaram': 173,
  'Marathahalli': 174,
  'Margondanahalli': 175,
  'Marsur': 176,
  'Mico Layout': 177,
  'Munnekollal': 178,
  'Murugeshpalya': 179,
  'Mysore Road': 180,
  'NGR Layout': 181,
  'NRI Layout': 182,
  'Nagadevanahalli': 183,
  'Naganathapura': 184,
  'Nagappa Reddy Layout': 185,
  'Nagarbhavi': 186,
  'Nagasandra': 187,
  'Nagavara': 188,
  'Nagavarapalya': 189,
  'Narayanapura': 190,
  'Neeladri Nagar': 191,
  'Nehru Nagar': 192,
  'OMBR Layout': 193,
  'Old Airport Road': 194,
  'Old Madras Road': 195,
  'Padmanabhanagar': 196,
  'Pai Layout': 197,
  'Panathur': 198,
  'Parappana Agrahara': 199,
  'Pattandur Agrahara': 200,
  'Poorna Pragna Layout': 201,
  'Prithvi Layout': 202,
  'R.T. Nagar': 203,
  'Rachenahalli': 204,
  'Raja Rajeshwari Nagar': 205,
  'Rajaji Nagar': 206,
  'Rajiv Nagar': 207,
  'Ramagondanahalli': 208,
  'Ramamurthy Nagar': 209,
  'Rayasandra': 210,
  'Sadashiva Nagar': 211,
  'Sahakara Nagar': 212,
  'Sanjay nagar': 213,
  'Sarakki Nagar': 214,
  'Sarjapur': 215,
  'Sarjapur  Road': 216,
  'Sarjapura - Attibele Road': 217,
  'Sector 1 HSR Layout': 218,
  'Sector 2 HSR Layout': 219,
  'Sector 7 HSR Layout': 220,
  'Seegehalli': 221,
  'Shampura': 222,
  'Shivaji Nagar': 223,
  'Singasandra': 224,
  'Somasundara Palya': 225,
  'Sompura': 226,
  'Sonnenahalli': 227,
  'Subramanyapura': 228,
  'Sultan Palaya': 229,
  'TC Palaya': 230,
  'Talaghattapura': 231,
  'Thanisandra': 232,
  'Thigalarapalya': 233,
  'Thubarahalli': 234,
  'Thyagaraja Nagar': 235,
  'Tindlu': 236,
  'Tumkur Road': 237,
  'Ulsoor': 238,
  'Uttarahalli': 239,
  'Varthur': 240,
  'Varthur Road': 241,
  'Vasanthapura': 242,
  'Vidyaranyapura': 243,
  'Vijayanagar': 244,
  'Vishveshwarya Layout': 245,
  'Vishwapriya Layout': 246,
  'Vittasandra': 247,
  'Whitefield': 248,
  'Yelachenahalli': 249,
  'Yelahanka': 250,
  'Yelahanka New Town': 251,
  'Yelenahalli': 252,
  'Yeshwanthpur': 253,
  'other': 254}

database=dataset.keys()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', estimated_price=0,locations=database)


@app.route('/predict', methods=['POST'])
def predict():

    # Code for processing the form data and calculating the estimated price
    location = request.form['location']
    bathrooms = float(request.form['bathrooms'])
    bedrooms = float(request.form['bedrooms'])
    area = float(request.form['area'])

    locationid=254     # by default consider it as others   
    for i in dataset:
        if location in i:
            locationid=dataset[i]
            break
    print(location)
    print(locationid)

    data = { 'location': [locationid],'total_sqft': [area],'bath': [bathrooms],'bhk': [bedrooms]}
    df = pd.DataFrame(data)

    estimated_price=int(model.predict(df.head(1))[0]*100000)
    final_value='{:,.0f}'.format(estimated_price)

   
    # return render_template('index.html',estimated_price=estimated_price,)
    return render_template('index.html',estimated_price=final_value)

if __name__ == '__main__':
    app.run(debug=True)

