from config import *

class LinkedinAutomation():
    def __init__(self) -> None:
        self.navegador = ""
        
        
        self.navegador = webdriver.Chrome(options=chrome_options, service=service)
        self.navegador.get('your_linkedin_url_here')
        self.navegador.maximize_window()

    def element_error(self, err, i):
        erro = type(err).__name__
        if erro == 'StaleElementReferenceException':
            print('Stale element: ', i)
        elif erro == 'ElementClickInterceptedException':
            print("Element click interception: ", i)
        else:
            print(erro)
        
    def Steps(self):
        time.sleep(3)
        self.navegador.find_element(By.CSS_SELECTOR, '#public_profile_contextual-sign-in > div > section > div > div > div > div.sign-in-modal > button').click()
        self.navegador.find_element(By.CSS_SELECTOR, '#public_profile_contextual-sign-in_sign-in-modal_session_key').send_keys('your_email')
        self.navegador.find_element(By.CSS_SELECTOR, '#public_profile_contextual-sign-in_sign-in-modal_session_password').send_keys('your_password')
        self.navegador.find_element(By.CSS_SELECTOR, '#public_profile_contextual-sign-in_sign-in-modal > div > section > div > div > form > div.flex.justify-between.sign-in-form__footer--full-width > button').click()

        time.sleep(5)
        self.navegador.find_element(By.CSS_SELECTOR, '#ember58').click()
        
        #search job position
        time.sleep(2)
        self.navegador.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(3) > a').click()

        time.sleep(2)
        barra_pesquisa = self.navegador.find_element(By.CSS_SELECTOR, '#global-nav-search > div')
        input = barra_pesquisa.find_elements(By.TAG_NAME, 'input')

        for i in input:
            atributo = i.get_attribute('aria-label')
            if atributo == 'Pesquisar cargo, competência ou empresa':
                i.send_keys('Engenheiro de Dados')
                break

        ActionChains(self.navegador, 10).send_keys(Keys.ENTER).perform()
        
        #Create your output file to recieve all data from webscrapping
        file = open("output.txt", "w", encoding='latin-1')
        
        num = 25

        time.sleep(5)
        while num <= 950:
            
            lista_vagas = self.navegador.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
            vagas = lista_vagas.find_elements(By.TAG_NAME, 'li')

            for vaga in vagas:
                try:
                    if vaga.get_attribute('id') != "": 
                        vaga.click()
                        time.sleep(3)
                    else: continue
                    
                    #descrição vagas
                    lis = self.navegador.find_element(By.ID, 'job-details')
                    vagas = lis.find_element(By.TAG_NAME, 'span')
                    job = vagas.find_elements(By.TAG_NAME, 'ul')
                    
                    for j in job:
                        file.write(j.text)
                        file.write("\n\n")
                    
                except Exception as err:
                    self.element_error(err, i)
            
            time.sleep(2)
            url = "https://www.linkedin.com/jobs/search/?currentJobId=3832130383&keywords=Engenheiro%20de%20Dados&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true&start=" + str(num)
            
            self.navegador.get(url)
            num += 25
            time.sleep(3)
            
        file.close()