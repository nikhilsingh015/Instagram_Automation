from selenium import webdriver
import time
from random import randint
import random
from selenium.webdriver.common.keys import Keys
from id import username, password
class InstaBot:

    #--------------------------------Login--------------------------------------------------------------
    def __init__(self, username, password):
       # driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(3)
    #    self.driver.close()
#--------------------------------Login Close--------------------------------------------------------------

#--------------------------------Get Followers New--------------------------------------------------------------
    def getUserFollowers(self, username, max):
        driver = self.driver
        driver.get('https://www.instagram.com/' + username)
        max = int(driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text)
        print("Total Followers =",max)
        iterations=int(max/12)
        followersLink = driver.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = driver.find_element_by_css_selector(
            'div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(
            followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(driver)
        #while (numberOfFollowersInList < max):
        for x in range(iterations):
            time.sleep(2)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(
                followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
            print ("Iteration",x)
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector(
                'a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers

        

#--------------------------------Get Followers New Close--------------------------------------------------------------


#--------------------------------Get Followers--------------------------------------------------------------
    def get_unfollowers(self, username):
        driver = self.driver
        driver.get("https://www.instagram.com/" + username + "/")
        time.sleep(2)
        allfoll = int(driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text)
        dialog= driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        print(allfoll)
        #scroll down the page
        for i in range(int(allfoll/2)):
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(randint(500, 1000)/1000)
            print("Extract friends %", round((i/(allfoll/2)*100), 2), "from", "%100")

#--------------------------------Get Followers Close--------------------------------------------------------------


#--------------------------------Close browser--------------------------------------------------------------
    def closeBrowser(self):
        self.driver.close()
#--------------------------------Close browser end--------------------------------------------------------------


#--------------------------------Testing--------------------------------------------------------------
    def testing(self):
        driver = self.driver
        driver.get("https://www.instagram.com/ankie_kar")
        time.sleep(4)
        followButton = driver.find_element_by_css_selector('button')
        time.sleep(2)
        print(followButton.text)
        time.sleep(2)
        #driver.find_element_by_xpath("//*[text()='Follow']").click()

#--------------------------------Testing end--------------------------------------------------------------

#--------------------------------Like Photos Mine--------------------------------------------------------------
    def likes(self, like, follow,lowtime,hightime):
        driver = self.driver
        #hashtags = []
        hashtags = ['love', 'instagood', 'photooftheday', 'fashion', 'beautiful', 'happy', 'cute', 'tbt', 'like4like',
                    'followme', 'picoftheday', 'follow', 'me', 'selfie’’, summer', 'art', 'instadaily', 'friends', 
                    'repost', 'nature', 'indian', 'mobilephotography', 'photography', 'roadtrips', 'travelmaharashtra',
                     'travelmumbai', 'travelpune', 'mumbai', 'streetfood', 'naturephotography', 'Pets', 'dogs', 'heavenonearth', 
                     'monsoon', 'ocean', 'indiafood', 'goa','lonavala','trekking','sunset','peace', 'calm', 'foodie',
                     'chicken','solotravel','traveldiaries','memories','travelmood', 'solo','Adventure','chill', 
                     'travelgram','mountains','tripping','boats', 'food','nonvegfood','street','Rains',
                     'naturelover','youtube','travelblog','travelblogger', 'traveldiaries','travel','vacations', 
                     'enjoying','travelpics','blogging','travelingsolo','solotrips','motivation','travelmotivation',
                     ]
        loop=0
        like = like/10
        follow = follow/10
        likecounter = 0
        folowcounter = 0
        randomnumber = 0
        internallikecount = 0
        itearaioncounter = 0
        sleep=0
        totalpostactions = random.randint(10, 20)
        print("Total post actions",totalpostactions)
        while loop < totalpostactions:
            loop = loop+1
            internallikecount=0
            tag = random.choice(hashtags)
            driver.get("https://www.instagram.com/explore/tags/" + tag + "/")
            time.sleep(2)
            try:
                driver.find_element_by_class_name("_9AhH0").click()
            except Exception:
                my_bot.likes(like,follow,lowtime,hightime)
                
            time.sleep(2)
            while internallikecount <10:
                itearaioncounter = itearaioncounter+1
                print("Total Iteration", itearaioncounter)
                internallikecount = internallikecount+1
                randomnumber = random.randint(1, 10)
                print("Random Number is ", randomnumber)

                if randomnumber <= like:
                    print("liking")
                    sleep = int(random.randint(lowtime, hightime))
                    print("Sleeping for ",sleep)
                    time.sleep(sleep)
                    if driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'):
                        driver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
                    #driver.find_elements_by_class_name('_8-yf5 ').click()
                    #driver.find_elements_by_css_selector('.\_8Rm4L:nth-child(1) .fr66n .\_8-yf5').click()
                    likecounter = likecounter+1
                    print("liked photo", likecounter)
                    
                if randomnumber <= follow:
                    followButton = driver.find_element_by_xpath(
                        "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
                    if (followButton.text != 'Following'):
                        print("Following")
                        #print(followButton.text)                        sleep = int(random.randint(lowtime, hightime))
                        print("Sleeping for ", sleep)
                        time.sleep(sleep)
                        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
                        folowcounter = folowcounter+1
                        print("folowcounter", folowcounter)
                    else:
                        print("You are already following this user")
                        continue

                driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
                time.sleep(random.randint(3, 7))
                print("Next")

            time.sleep(2)
            hashtags.remove(tag)
        print("total Photos Liked : ",likecounter) 
        print("total Folows: ", folowcounter)

            
            
#--------------------------------Like Photos Mine End--------------------------------------------------------------

#--------------------------------Main--------------------------------------------------------------
my_bot = InstaBot(username, password)
#my_bot = InstaBot('nikhil.singh.94', 'Mum_mar2020')
#my_bot.get_unfollowers('travelwith_thelazynick')
#my_bot.Photolikes()
like=4
follow=3
lowtime=7
hightime=12
#my_bot.likes(like,follow,lowtime,hightime)
#my_bot.getUserFollowers(username,500)
#my_bot.testing()
 



