import requests
from bs4 import BeautifulSoup

class Ottawa_Animals():

    def dogs(self):
            
        updated_info_list_np =[]

        url = "https://ottawahumane.ca/adopt/dogs-for-adoption/?orderby=date"
        while url:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            
            names_list = []
            info_list = []

            
            names = soup.find_all("div", class_="info-card__title")
            for x in names:
                name = x.text.strip().replace("Name | ", "")
                names_list.append(name)

            info = soup.find_all("li", class_="info-card__item")
            for j in info:
                info = j.text.strip()
                info_list.append(info)
            
            
            for k in range(len(names_list)):
                k_index = k * 5
                dog_info_list = []
                if k_index + 4 < len(info_list):
                    dog_info_list.append(info_list[k_index])
                    dog_info_list.append(info_list[k_index + 1])
                    dog_info_list.append(info_list[k_index + 2])
                    dog_info_list.append(info_list[k_index + 3])
                    dog_info_list.append(info_list[k_index + 4])
                    dog_info_list.insert(0, names_list[k])
                    updated_info_list_np.append(dog_info_list)
            
            
            np = soup.find("a", class_="next pagination__link")
            if np:
                url = np.get('href')
            else:
                url = None
        return(updated_info_list_np)

    def cats(self):
        
        url = "https://ottawahumane.ca/adopt/cats-for-adoption/?_gl=1*1dgy9br*_ga*MTE5NTc1ODE3Ny4xNzA1MTg1NDA1*_ga_JLNZ53SJ3K*MTcwNTMzMDM0NC40LjEuMTcwNTMzMDM0Ny4wLjAuMA..*_gcl_au*MTY4Mzg0NDkzOC4xNzA1MTg1NDA1*_ga_Z8C7JLHLGE*MTcwNTMzMDM0NC40LjEuMTcwNTMzMDM0Ny41Ny4wLjA."
        updated_cat_info_list_np = []

        while url:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            
            cat_names_list = []
            c_info_list = []

            cat_names = soup.find_all("div", class_="info-card__title")
            for x in cat_names:
                cat_name = x.text.strip().replace("Name | ", "")
                cat_names_list.append(cat_name)

            cat_info = soup.find_all("li", class_="info-card__item")
            for j in cat_info:
                info = j.text.strip()
                c_info_list.append(info)
            
            for k in range(len(cat_names_list)):
                k_index = k * 5
                cat_info_list = []
                if k_index + 4 < len(c_info_list):
                    cat_info_list.append(c_info_list[k_index])
                    cat_info_list.append(c_info_list[k_index + 1])
                    cat_info_list.append(c_info_list[k_index + 2])
                    cat_info_list.append(c_info_list[k_index + 3])
                    cat_info_list.append(c_info_list[k_index + 4])
                    cat_info_list.insert(0, cat_names_list[k])
                    updated_cat_info_list_np.append(cat_info_list)
            
            np = soup.find("a", class_="next pagination__link")
            if np:
                url = np.get('href')
            else:
                url = None

        return(updated_cat_info_list_np)

class Toronto_Animals():

    def dogs(self):
        req = requests.get("https://24petconnect.com/TorontoAdoptablePets?at=DOG")
        soup = BeautifulSoup(req.text, "html.parser")

        dog_names_list = []
        dog_gender_list = []
        dog_id_list =[]
        dog_breed_list =[]
        dog_age_list =[]
        completeDog_List = []

        dog_names = soup.find_all("span", class_="text_Name results")
        for x in dog_names:
            dog_names = x.text.strip()

            start_index = dog_names.find('(') + 1
            end_index = dog_names.find(')', start_index)
            
            if start_index != -1 and end_index != -1:
                dog_id = dog_names[start_index:end_index]
                dog_names = dog_names.replace(" (" + dog_id + ")", "")
                dog_id_list.append("Animal ID: " + dog_id)
            dog_names_list.append(dog_names.capitalize())
        

        dog_gender = soup.find_all("span", class_="text_Gender results")
        for j in dog_gender:
            dog_gender = j.text.strip()
            dog_gender = dog_gender.split()[1]
            dog_gender_list.append("Sex: " + dog_gender)

        dog_breed = soup.find_all("span", class_="text_Breed results")
        for k in dog_breed:
            dog_breed = k.text.strip()
            dog_breed_list.append("Breed: " + dog_breed)
        
        dog_age = soup.find_all("span", class_="text_Age results")
        for u in dog_age:
            dog_age = u.text.strip()
            dog_age_list.append("Age: " + dog_age)
        
        for e in range(len(dog_names_list)):
            dog_info_list = []
            dog_info_list.append(dog_names_list[e])
            dog_info_list.append(dog_breed_list[e])
            dog_info_list.append(dog_age_list[e])
            dog_info_list.append(dog_gender_list[e])
            dog_info_list.append(dog_id_list[e])
            completeDog_List.append(dog_info_list)

        return(completeDog_List)

    def cats(self):
        req = requests.get("https://24petconnect.com/TorontoAdoptablePets?at=CAT")
        soup = BeautifulSoup(req.text, "html.parser")

        cat_names_list = []
        cat_gender_list = []
        cat_id_list =[]
        cat_breed_list =[]
        cat_age_list =[]
        completeCat_List = []

        cat_names = soup.find_all("span", class_="text_Name results")
        for x in cat_names:
            cat_names = x.text.strip()

            start_index = cat_names.find('(') + 1
            end_index = cat_names.find(')', start_index)
            
            if start_index != -1 and end_index != -1:
                cat_id = cat_names[start_index:end_index]
                cat_names = cat_names.replace(" (" + cat_id + ")", "")
                cat_id_list.append("Animal ID: " + cat_id)
            cat_names_list.append(cat_names.capitalize())
        

        cat_gender = soup.find_all("span", class_="text_Gender results")
        for j in cat_gender:
            cat_gender = j.text.strip()
            cat_gender = cat_gender.split()[1]
            cat_gender_list.append("Sex: " + cat_gender)

        cat_breed = soup.find_all("span", class_="text_Breed results")
        for k in cat_breed:
            cat_breed = k.text.strip()
            cat_breed_list.append("Breed: " + cat_breed)
        
        cat_age = soup.find_all("span", class_="text_Age results")
        for u in cat_age:
            cat_age = u.text.strip()
            cat_age_list.append("Age: " + cat_age)
        
        for e in range(len(cat_names_list)):
            cat_info_list = []
            cat_info_list.append(cat_names_list[e])
            cat_info_list.append(cat_breed_list[e])
            cat_info_list.append(cat_age_list[e])
            cat_info_list.append(cat_gender_list[e])
            cat_info_list.append(cat_id_list[e])
            completeCat_List.append(cat_info_list)
            
        return(completeCat_List)

def main():
    animal_shelter = None

    while True:
        city = input("Enter a city (Ottawa or Toronto): ")
        if city.upper() == "OTTAWA":
            animal_shelter = Ottawa_Animals()
            break
        elif city.lower() == 'toronto':
            animal_shelter = Toronto_Animals()
            break
        else:
            print("Invalid city entered.")
    
    while True:
        animal = input("Enter the animal type (Dog or Cat): ")
        if animal.upper() in ["DOG", "DOGS"]:
            if animal_shelter:
                animals_info = animal_shelter.dogs()
            break
        elif animal.upper() in ["CAT", "CATS"]:
            if animal_shelter:
                animals_info = animal_shelter.cats()
            break
        else:
            print("Invalid animal type entered.")

    for animal_info in animals_info:
        print("\n")
        for info in animal_info:
            print(info)

main()