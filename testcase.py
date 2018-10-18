import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TCMMovieDataBaseTestSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_movie_search_info(self):
        URL = "http://www.tcm.com/tcmdb/"
        WAIT = 20
        driver = self.driver
        driver.get(URL)

        movielist = [link.get_attribute('href') for link in driver.find_elements_by_xpath("//div[@id='movieSearchList']//div[@class='theList']/a")]
        movieTitle = [title.get_attribute('text') for title in driver.find_elements_by_xpath("//div[@id='movieSearchList']//div[@class='theList']/a")]
        index =0
        if len(movielist) == 10 :
            for movie in movielist[:5] :
                    print "Hyperlink Text:" + movieTitle[index]
                    index = +1
                    driver.get(movie)
                    WebDriverWait(driver, WAIT)
                    moiveheader = driver.find_element_by_xpath("//div[@id='dbartimgtitle']//h1")
                    print "Movie Details: " +  moiveheader.text
                    assert not moiveheader.text =="" "Movie Title is missing"
                    movieOverview = driver.find_element_by_xpath("//div[@class='expandbox h1bsynop']//p[@class='bsynopsis']")
                    print "Movie Overview: " +  movieOverview.text
                    assert not movieOverview.text =="" "Movie Overview is missing"
                    crew =driver.find_elements_by_xpath("//div[@id='overViewbox']//div//div//div/strong/a")
                    if len(crew) > 2 :
                       print "Crew1:" + crew[0].text
                       assert not crew[0].text =="" "Crew 1/actor is not found"
                       print not "Crew2:" + crew[1].text
                       assert not crew[1].text =="" "Crew 2/actor is not found"

                    additonalDetails = driver.find_elements_by_xpath("//table[@class='dvd-add-details tbl1']//tbody//tr")
                    for deailtsrow in additonalDetails :
                        cell = deailtsrow.find_elements_by_tag_name("td")
                        if len(cell) >2:
                            strcell = str(cell[0].text)
                            if "Release Date" in strcell:
                                print "Release Label :" + cell[0].text
                                assert not cell[0].text =="" "Release date text is missing"
                                print "Release Date :" + cell[1].text
                                assert not cell[1].text =="" "Release date is missing"
                                break

                    driver.execute_script("window.history.go(-1)")
                    WebDriverWait(driver, WAIT)

        else :
            assert "No results found." not in driver.page_source

        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()