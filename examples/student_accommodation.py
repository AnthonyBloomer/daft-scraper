from daftlistings import Daft, SortOrder, SortType, RentType, University, StudentAccommodationType

offset = 0

while True:
    daft = Daft()
    daft.set_listing_type(RentType.STUDENT_ACCOMMODATION)
    daft.set_university(University.NCI)
    daft.set_student_accommodation_type(StudentAccommodationType.ROOM_TO_SHARE)
    daft.set_min_price(500)
    daft.set_max_price(700)
    daft.set_sort_by(SortType.PRICE)
    daft.set_sort_order(SortOrder.ASCENDING)
    daft.set_offset(offset)
    listings = daft.get_listings()

    if len(listings) == 0:
        break

    for listing in listings:
        print listing.get_price()
        print listing.get_formalised_address()
        print listing.get_daft_link()

    offset += 10