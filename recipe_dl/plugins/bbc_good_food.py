class Plugin():

    # Plugin name as a string
    name = "BBC Good Food"

    # Plugin website URL as string
    website = "www.bbcgoodfood.com"


    def __init__(self):
        pass


    def parse(self, tree):

        name = tree.xpath('//header/h1/text()')[0]
        prep_time = tree.xpath('//span[@class="cooking-time-prep"]/span/text()')
        cook_time = tree.xpath('//span[@class="cooking-time-cook"]/span/text()')
        ingredients = tree.xpath('//ul[@class="unstyled"]/li/text()')
        method = tree.xpath('//ol[@class="unstyled"]/li/span/text()')

        recipe_dict = {

            "name" : name,
            "prep_time" : prep_time,
            "cook_time" : cook_time,
            "ingredients" : ingredients,
            "method" : method,
            # "image" : image,
        }

        return recipe_dict


    def meta(self):

        meta_dict = {
            "name" : self.name,
            "website" : self.website,
        }

        return meta_dict

