class Plugin():

    # Plugin name as a string
    name = "River Cottage"

    # Plugin website URL as string
    website = "www.rivercottage.net"


    def __init__(self):
        pass


    def parse(self, tree):

        name = tree.xpath('//h1/text()')[0]
        timings = tree.xpath('//span[@class="recipe-stat recipe-stat--large"]/span/span/span/text()')
        ingredients = tree.xpath('//div[@class="[ ingredients__list ] [ formatted ]"]/ul/li/text()')
        method = tree.xpath('//div[@class="[ formatted ] [ recipe-detail__content ]"]/p/text()')

        recipe_dict = {

            "name" : name,
            "prep_time" : timings[0],
            "cook_time" : timings[1],
            "ingredients" : ingredients,
            "method" : method,
        }

        return recipe_dict


    def meta(self):

        meta_dict = {
            "name" : self.name,
            "website" : self.website,
        }

        return meta_dict

