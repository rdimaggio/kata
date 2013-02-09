import csv


class Checkout():
    #@profile
    def __init__(self, rules_file, item_column=0, price_column=1,
                 quantity_column=2):
        # open file
        csvfile = csv.reader(open(rules_file, 'rU'))
        # pull off header
        header = csvfile.next()
        # pricing dictionary
        self.prices = {}
        # load in pricing rules
        for row in csvfile:
            lower_item = row[item_column].lower()
            # ASSUMPTION: different quantity dicounts will not be provided
            # add price entry to quantity dictionary
            if lower_item in self.prices:
                self.prices[lower_item][int(row[quantity_column])] = \
                    float(row[price_column])
            # create initial price entry
            else:
                self.prices[lower_item] = {int(row[quantity_column]):
                                           float(row[price_column])}
        # scanned items dictionary
        self.scanned_items = {}

    #@profile
    def scan(self, item):
        # increment quantity
        lower_item = item.lower()
        if lower_item in self.scanned_items:
            self.scanned_items[lower_item] += 1
        # initial quantity
        else:
            self.scanned_items[lower_item] = 1

    def scan_list(self, item_list):
        for item in item_list:
            self.scan(item.lower())

    #@profile
    def unscan(self, item):
        lower_item = item.lower()
        # decrement quantity
        if lower_item in self.scanned_items:
            if self.scanned_items[lower_item] < 1:
                self.scanned_items[lower_item] = 0
            else:
                self.scanned_items[lower_item] -= 1
        # item never scanned before
        else:
            print "Item: " + item + " was never scanned"

    #@profile
    def best_price(self, item, quantity):
        # ASSUMPTION: higher volume discounts have cheaper unit costs
        # get best quantity discount match
        try:
            disc_qty = max([x for x in self.prices[item].keys()
                           if x <= quantity])
            return disc_qty, self.prices[item][disc_qty]
        except KeyError:
            print "No price for: " + item + " exists in the system"
            return quantity, 0

    #@profile
    def total(self):
        total = 0
        # calculate price for each item
        for item in self.scanned_items.keys():
            quantity = self.scanned_items[item]
            # loop through volume discounts
            while quantity:
                disc_qty, price = self.best_price(item, quantity)
                # if no discount, no need to continue looping
                if disc_qty == 1:
                    total += quantity * price
                    quantity = 0
                # calculate discount and reduce quantity still to calculate
                else:
                    total += disc_qty * price
                    quantity -= disc_qty

        # round floating point result
        return int("%.0f" % total)


if __name__ == '__main__':
    ITEM_COLUMN = 0
    PRICE_COLUMN = 1
    QUANTITY_COLUMN = 2
    RULES_FILE = 'rules.csv'

    co = Checkout(RULES_FILE, ITEM_COLUMN, PRICE_COLUMN, QUANTITY_COLUMN)
    co.scan("A")
    co.scan("B")
    co.scan("B")
    co.unscan("B")
    co.scan("A")
    co.scan("C")
    co.scan("A")
    co.scan("A")
    co.scan("B")
    co.scan("B")
    co.scan("D")
    co.scan("E")
    print co.total()
