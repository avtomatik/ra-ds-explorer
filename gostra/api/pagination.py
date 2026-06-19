def paginate(first_page, fetch_page):
    page = first_page

    while True:

        yield from page.items

        next_link = page.links.next

        if not next_link:
            break

        page = fetch_page(next_link.href)
