# Registering people for workshops, courses, and trainings

The most robust, no-extra-cost way to take registrations is **Shopify's own
products and checkout**. Each offering becomes a product; registering *is*
adding the seat to the cart and checking out. This handles payment, seat limits,
confirmation emails, and a record of who registered, with no third-party app.

## How it works

1. **Create a product per offering** (Admin > Products > Add product).
   - Title = the workshop/course/training name.
   - Price = the registration fee (set to 0 for free; or use a free product).
   - Under **Inventory**, enable "Track quantity" and set the quantity to the
     **number of seats**. When seats sell out, the button shows "Sold Out"
     automatically.
   - Add the date/time/location to the description.
   - Optional: put these products in a **Collection** (e.g. "Workshops",
     "Courses", "Trainings") so they can be listed together.

2. **Surface them on a page** in either of two ways:
   - **Workshops & events section**: each event block has a **"Register via
     product"** picker. Select the product, and the card shows the price and a
     **Register** button that adds the seat and goes to checkout. Seat limits
     come from the product's inventory; sold-out events say so.
   - **Collection page**: assign the `collection` template to a collection of
     offerings to show them as a grid that links to each product's page.

3. **People register** by clicking Register and completing checkout. You get the
   order (name, email, payment) in Admin > Orders. Export anytime.

## Free events
Set the product price to 0. Checkout still captures name and email, giving you a
roster, without charging a card.

## Recurring sessions / dates
Use product **variants** for dates (e.g. "June 12", "July 9") or create one
product per date. Each variant/product carries its own seat inventory.

## Digital courses (downloads / access)
For self-paced courses, sell a product and deliver access with a digital-product
app or a link in the order confirmation. The `product` template supports this.

## Alternatives (and why product-based is usually better)
- **Eventbrite** (currently used for some groups): fine for free community
  events, but takes fees and sends people off-site. Keep the external-link field
  on event blocks if you want to point to Eventbrite for specific items.
- **Cowlendar / booking apps** (installed on the old store): better for
  *appointment* booking (1:1 time slots) than for fixed-seat group events.
- **Shopify products**: best for paid, seat-limited workshops/courses/trainings,
  keeps registration, payment, and records in one place, on-brand, no fees
  beyond Shopify's normal payment processing.

## Quick checklist
- [ ] Product created per offering, with price and seat inventory
- [ ] (Optional) Offerings grouped into a Collection
- [ ] Event blocks linked to their products (Workshops & events section)
- [ ] Test a registration end to end (add to cart > checkout > order appears)
- [ ] Confirm sold-out behavior by setting inventory to 0
