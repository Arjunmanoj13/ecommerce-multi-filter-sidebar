import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Nexora | Find your next favorite",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #172B75;
        --yellow: #FFE500;
        --page: #F1F3F6;
        --ink: #172033;
        --muted: #687386;
        --line: #E6EAF0;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background: var(--page);
        color: var(--ink);
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid var(--line);
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.75rem;
    }
    .block-container {
        max-width: 1440px;
        padding-top: 1.15rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3, p {
        letter-spacing: -0.02em;
    }
    .brand-mark {
        color: var(--navy);
        font-size: 1.45rem;
        font-weight: 800;
        letter-spacing: -0.06em;
        white-space: nowrap;
    }
    .brand-mark span {
        color: #E2B900;
    }
    .hero {
        background: linear-gradient(112deg, #172B75 0%, #27469D 62%, #4164BD 100%);
        border-radius: 20px;
        color: white;
        margin: 0.75rem 0 1.4rem;
        min-height: 210px;
        overflow: hidden;
        padding: 2rem 2.4rem;
        position: relative;
    }
    .hero:after {
        background: radial-gradient(circle, rgba(255,229,0,.2), transparent 68%);
        content: "";
        height: 330px;
        position: absolute;
        right: 3%;
        top: -75px;
        width: 330px;
    }
    .hero-kicker {
        color: #FFE500;
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .13em;
        text-transform: uppercase;
    }
    .hero h1 {
        color: white;
        font-size: clamp(1.8rem, 3.2vw, 2.7rem);
        line-height: 1.12;
        margin: .55rem 0;
        max-width: 650px;
    }
    .hero p {
        color: rgba(255,255,255,.82);
        font-size: 1rem;
        margin: 0;
    }
    .section-heading {
        color: var(--ink);
        font-size: 1.45rem;
        font-weight: 750;
        margin: .3rem 0 .1rem;
    }
    .section-caption {
        color: var(--muted);
        font-size: .9rem;
        margin-bottom: .8rem;
    }
    .product-name {
        color: var(--ink);
        font-size: 1rem;
        font-weight: 700;
        line-height: 1.35;
        min-height: 2.7rem;
        margin-top: .5rem;
    }
    .product-meta {
        color: var(--muted);
        font-size: .82rem;
        margin: .18rem 0;
    }
    .rating-line {
        color: #8A6500;
        font-size: .86rem;
        margin: .45rem 0;
    }
    .price-line {
        align-items: baseline;
        display: flex;
        flex-wrap: wrap;
        gap: .45rem;
        margin: .5rem 0;
    }
    .sale-price {
        color: #18233C;
        font-size: 1.2rem;
        font-weight: 800;
    }
    .original-price {
        color: #8A93A2;
        font-size: .86rem;
        text-decoration: line-through;
    }
    .discount-badge {
        background: #FFF4C2;
        border-radius: 999px;
        color: #765B00;
        display: inline-block;
        font-size: .72rem;
        font-weight: 700;
        padding: .3rem .6rem;
    }
    .stock-in {
        color: #16834A;
        font-size: .8rem;
        font-weight: 600;
    }
    .stock-out {
        color: #B54747;
        font-size: .8rem;
        font-weight: 600;
    }
    .image-fallback {
        align-items: center;
        background: #F5F7FA;
        border-radius: 12px;
        color: #8792A2;
        display: flex;
        font-size: 3rem;
        height: 190px;
        justify-content: center;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: white;
        border: 1px solid var(--line);
        border-radius: 15px;
        box-shadow: 0 5px 18px rgba(27, 44, 80, .045);
        height: 100%;
        padding: .65rem .75rem .8rem;
        transition: box-shadow .2s ease, transform .2s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        box-shadow: 0 10px 24px rgba(27, 44, 80, .10);
        transform: translateY(-2px);
    }
    .stButton > button {
        border-radius: 9px;
        font-weight: 650;
        min-height: 2.45rem;
    }
    .stButton > button[kind="primary"] {
        background: var(--yellow);
        border: 1px solid #E5CF00;
        color: #18233C;
    }
    .stButton > button[kind="primary"]:hover {
        background: #F2D900;
        border-color: #D7C000;
        color: #18233C;
    }
    [data-testid="stPopover"] > button {
        border-color: transparent;
        color: var(--navy);
        font-weight: 650;
        white-space: nowrap;
    }
    [data-testid="stTextInput"] input {
        border-radius: 10px;
    }
    [data-testid="stMarkdownContainer"] a {
        color: var(--navy);
    }
    @media (max-width: 800px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .hero {
            min-height: 180px;
            padding: 1.5rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


products = pd.DataFrame(
    [
        [1, "Samsung Galaxy S24", "Samsung", "Mobiles", 45000, 52999, 15, 4.5, 3280, "Black", True, 97, "📱", "https://images.unsplash.com/photo-1511709268805-e6a2b3a5f8c4?auto=format&fit=crop&w=800&q=85"],
        [2, "iPhone 15", "Apple", "Mobiles", 65000, 74900, 13, 4.8, 5120, "Blue", True, 100, "📱", "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?auto=format&fit=crop&w=800&q=85"],
        [3, "OnePlus 12", "OnePlus", "Mobiles", 55000, 64999, 15, 4.4, 1840, "Green", True, 90, "📱", "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=800&q=85"],
        [4, "HP Pavilion", "HP", "Laptops", 65000, 74999, 13, 4.2, 960, "Silver", True, 82, "💻", "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=800&q=85"],
        [5, "MacBook Air M3", "Apple", "Laptops", 110000, 119900, 8, 4.9, 2710, "Silver", True, 99, "💻", "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=85"],
        [6, "Dell Inspiron", "Dell", "Laptops", 58000, 69999, 17, 4.1, 740, "Black", False, 68, "💻", "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=800&q=85"],
        [7, "Nike Air Max", "Nike", "Shoes", 8000, 10995, 27, 4.3, 4320, "White", True, 95, "👟", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=85"],
        [8, "Adidas Ultraboost", "Adidas", "Shoes", 12000, 14999, 20, 4.6, 2190, "Black", True, 92, "👟", "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=800&q=85"],
        [9, "Puma Runner", "Puma", "Shoes", 5000, 6999, 29, 3.9, 610, "Blue", False, 61, "👟", "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&w=800&q=85"],
        [10, "Sony Headphones", "Sony", "Accessories", 12000, 14990, 20, 4.7, 1960, "Black", True, 91, "🎧", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=85"],
        [11, "Boat Earbuds", "Boat", "Accessories", 2000, 2999, 33, 4.0, 3460, "White", True, 94, "🎧", "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?auto=format&fit=crop&w=800&q=85"],
        [12, "JBL Speaker", "JBL", "Accessories", 6000, 7999, 25, 4.4, 1230, "Blue", True, 84, "🔊", "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=800&q=85"],
    ],
    columns=[
        "ID",
        "Name",
        "Brand",
        "Category",
        "Price",
        "OriginalPrice",
        "Discount",
        "Rating",
        "Reviews",
        "Color",
        "InStock",
        "Popularity",
        "Icon",
        "ImageURL",
    ],
)

price_min = int(products["Price"].min())
price_max = int(products["Price"].max())
filter_defaults = {
    "search_query": "",
    "category_filter": [],
    "brand_filter": [],
    "price_filter": (price_min, price_max),
    "rating_filter": 0.0,
    "color_filter": [],
    "stock_filter": False,
    "discount_filter": 0,
    "sort_option": "Default",
}

for state_key, default_value in filter_defaults.items():
    st.session_state.setdefault(state_key, default_value)
st.session_state.setdefault("cart", {})
st.session_state.setdefault("wishlist", [])


def reset_filter(state_key):
    st.session_state[state_key] = filter_defaults[state_key]


def reset_filters():
    for state_key, default_value in filter_defaults.items():
        st.session_state[state_key] = default_value


def select_category(category):
    st.session_state["category_filter"] = [category] if category else []


def remove_selected_value(state_key, value):
    st.session_state[state_key] = [
        item for item in st.session_state[state_key] if item != value
    ]


def add_to_cart(product_id):
    cart = dict(st.session_state["cart"])
    cart[product_id] = cart.get(product_id, 0) + 1
    st.session_state["cart"] = cart


def change_cart_quantity(product_id, amount):
    cart = dict(st.session_state["cart"])
    updated_quantity = cart.get(product_id, 0) + amount
    if updated_quantity <= 0:
        cart.pop(product_id, None)
    else:
        cart[product_id] = updated_quantity
    st.session_state["cart"] = cart


def remove_from_cart(product_id):
    cart = dict(st.session_state["cart"])
    cart.pop(product_id, None)
    st.session_state["cart"] = cart


def toggle_wishlist(product_id):
    wishlist = list(st.session_state["wishlist"])
    if product_id in wishlist:
        wishlist.remove(product_id)
    else:
        wishlist.append(product_id)
    st.session_state["wishlist"] = wishlist


def render_product_image(product):
    image_url = product.get("ImageURL")
    if isinstance(image_url, str) and image_url.strip():
        try:
            st.image(image_url, use_container_width=True)
            return
        except (OSError, ValueError):
            pass
    st.markdown(
        f"<div class='image-fallback'>{product['Icon']}</div>",
        unsafe_allow_html=True,
    )


def render_product_card(product, card_context):
    product_id = int(product["ID"])
    with st.container(border=True):
        badge_col, heart_col = st.columns([1.3, 1], vertical_alignment="center")
        with badge_col:
            st.markdown(
                f"<span class='discount-badge'>{int(product['Discount'])}% OFF</span>",
                unsafe_allow_html=True,
            )
        with heart_col:
            is_wishlisted = product_id in st.session_state["wishlist"]
            st.button(
                "♥ Saved" if is_wishlisted else "♡ Wishlist",
                key=f"wishlist_{card_context}_{product_id}",
                on_click=toggle_wishlist,
                args=(product_id,),
                use_container_width=True,
            )

        render_product_image(product)
        st.markdown(
            f"<div class='product-name'>{product['Name']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='product-meta'>{product['Brand']} &nbsp;·&nbsp; {product['Category']} &nbsp;·&nbsp; {product['Color']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='rating-line'>★ {product['Rating']} <span style='color:#8992A0'>({int(product['Reviews']):,} reviews)</span></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='price-line'><span class='sale-price'>₹{int(product['Price']):,}</span>"
            f"<span class='original-price'>₹{int(product['OriginalPrice']):,}</span></div>",
            unsafe_allow_html=True,
        )
        stock_class = "stock-in" if product["InStock"] else "stock-out"
        stock_text = "In stock" if product["InStock"] else "Currently unavailable"
        st.markdown(
            f"<div class='{stock_class}'>{stock_text}</div>",
            unsafe_allow_html=True,
        )
        st.button(
            "Add to cart",
            key=f"add_cart_{card_context}_{product_id}",
            type="primary",
            use_container_width=True,
            disabled=not bool(product["InStock"]),
            on_click=add_to_cart,
            args=(product_id,),
        )


def render_cart_contents():
    cart = st.session_state["cart"]
    if not cart:
        st.caption("Your cart is waiting for something good.")
        return

    subtotal = 0
    for product_id, quantity in list(cart.items()):
        product = products.loc[products["ID"] == product_id].iloc[0]
        line_total = int(product["Price"]) * quantity
        subtotal += line_total
        st.markdown(f"**{product['Name']}**  ·  ₹{int(product['Price']):,} each")
        quantity_cols = st.columns([1, 1, 1, 2])
        quantity_cols[0].button(
            "−",
            key=f"cart_decrease_{product_id}",
            on_click=change_cart_quantity,
            args=(product_id, -1),
        )
        quantity_cols[1].markdown(
            f"<div style='padding:.55rem 0;text-align:center'>{quantity}</div>",
            unsafe_allow_html=True,
        )
        quantity_cols[2].button(
            "+",
            key=f"cart_increase_{product_id}",
            on_click=change_cart_quantity,
            args=(product_id, 1),
        )
        quantity_cols[3].button(
            "Remove",
            key=f"cart_remove_{product_id}",
            on_click=remove_from_cart,
            args=(product_id,),
        )
    st.divider()
    st.markdown(f"**Subtotal** <span style='float:right'>₹{subtotal:,}</span>", unsafe_allow_html=True)
    st.markdown("**Shipping** <span style='float:right'>Free</span>", unsafe_allow_html=True)
    st.markdown(f"### Total  ·  ₹{subtotal:,}")


def render_wishlist_contents():
    wishlist = st.session_state["wishlist"]
    if not wishlist:
        st.caption("Save products with the heart button to find them here.")
        return

    for product_id in list(wishlist):
        product = products.loc[products["ID"] == product_id].iloc[0]
        item_col, remove_col = st.columns([3, 1])
        item_col.markdown(
            f"**{product['Name']}**<br><span style='color:#687386'>₹{int(product['Price']):,}</span>",
            unsafe_allow_html=True,
        )
        remove_col.button(
            "♥",
            key=f"wishlist_remove_{product_id}",
            help=f"Remove {product['Name']} from wishlist",
            on_click=toggle_wishlist,
            args=(product_id,),
        )


def format_price_range(price_range):
    return f"₹{price_range[0]:,}–₹{price_range[1]:,}"


cart_item_count = sum(st.session_state["cart"].values())
navbar_cols = st.columns([1.35, 4.8, 1.0, 1.15, 1.05], gap="small")
with navbar_cols[0]:
    st.markdown(
        "<div class='brand-mark'>NEX<span>ORA</span></div>",
        unsafe_allow_html=True,
    )
with navbar_cols[1]:
    st.text_input(
        "Search products",
        key="search_query",
        placeholder="Search products, brands and categories",
        label_visibility="collapsed",
    )
with navbar_cols[2]:
    with st.popover("Account", use_container_width=True):
        st.markdown("### Welcome to Nexora")
        st.caption("Your shopping, your way.")
        st.write(f"🛒 Cart items: **{cart_item_count}**")
        st.write(f"♡ Saved products: **{len(st.session_state['wishlist'])}**")
with navbar_cols[3]:
    with st.popover(
        f"♡ Wishlist ({len(st.session_state['wishlist'])})",
        use_container_width=True,
    ):
        st.markdown("### Your wishlist")
        render_wishlist_contents()
with navbar_cols[4]:
    with st.popover(f"🛒 Cart ({cart_item_count})", use_container_width=True):
        st.markdown("### Your cart")
        render_cart_contents()

categories = sorted(products["Category"].unique())
category_cols = st.columns(len(categories) + 1, gap="small")
with category_cols[0]:
    st.button(
        "All departments",
        key="category_nav_all",
        use_container_width=True,
        on_click=select_category,
        args=("",),
    )
for index, category in enumerate(categories, start=1):
    with category_cols[index]:
        st.button(
            category,
            key=f"category_nav_{category}",
            use_container_width=True,
            on_click=select_category,
            args=(category,),
        )

st.markdown(
    """
    <section class="hero">
      <div class="hero-kicker">The good-find edit</div>
      <h1>Everyday favorites.<br>Prices worth a second look.</h1>
      <p>Discover trusted tech, style and essentials — with savings up to 33%.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("## Refine your search")
st.sidebar.caption("Choose any combination of filters.")
st.sidebar.button(
    "Clear all filters",
    key="clear_all_filters",
    use_container_width=True,
    on_click=reset_filters,
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    key="category_filter",
)
brands = sorted(products["Brand"].unique())
selected_brands = st.sidebar.multiselect(
    "Brand",
    brands,
    key="brand_filter",
)
price_range = st.sidebar.slider(
    "Price range (₹)",
    min_value=price_min,
    max_value=price_max,
    key="price_filter",
    step=1000,
)
min_rating = st.sidebar.selectbox(
    "Minimum customer rating",
    [0.0, 1.0, 2.0, 3.0, 4.0, 4.5],
    format_func=lambda value: "Any rating" if value == 0 else f"{value:g} stars & up",
    key="rating_filter",
)
colors = sorted(products["Color"].unique())
selected_colors = st.sidebar.multiselect(
    "Available colors",
    colors,
    key="color_filter",
)
in_stock = st.sidebar.checkbox("Show only in-stock products", key="stock_filter")
min_discount = st.sidebar.slider(
    "Minimum discount",
    min_value=0,
    max_value=50,
    key="discount_filter",
    format="%d%%",
)

sort_option = st.selectbox(
    "Sort products by",
    ["Default", "Price: Low to High", "Price: High to Low", "Highest Rated", "Most Popular"],
    key="sort_option",
)

filtered = products.copy()
search_query = st.session_state["search_query"].strip()
if search_query:
    searchable_fields = ["Name", "Brand", "Category", "Color"]
    search_match = pd.Series(False, index=filtered.index)
    for field in searchable_fields:
        search_match |= filtered[field].str.contains(
            search_query,
            case=False,
            na=False,
            regex=False,
        )
    filtered = filtered[search_match]
if selected_categories:
    filtered = filtered[filtered["Category"].isin(selected_categories)]
if selected_brands:
    filtered = filtered[filtered["Brand"].isin(selected_brands)]
filtered = filtered[
    (filtered["Price"] >= price_range[0])
    & (filtered["Price"] <= price_range[1])
]
filtered = filtered[filtered["Rating"] >= min_rating]
if selected_colors:
    filtered = filtered[filtered["Color"].isin(selected_colors)]
if in_stock:
    filtered = filtered[filtered["InStock"]]
if min_discount:
    filtered = filtered[filtered["Discount"] >= min_discount]

if sort_option == "Price: Low to High":
    filtered = filtered.sort_values("Price")
elif sort_option == "Price: High to Low":
    filtered = filtered.sort_values("Price", ascending=False)
elif sort_option == "Highest Rated":
    filtered = filtered.sort_values("Rating", ascending=False)
elif sort_option == "Most Popular":
    filtered = filtered.sort_values("Popularity", ascending=False)

st.markdown("<div class='section-heading'>Featured products</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-caption'>Customer favorites, hand-picked for you.</div>",
    unsafe_allow_html=True,
)
featured_products = products.sort_values("Popularity", ascending=False).head(4)
featured_cols = st.columns(4, gap="medium")
for index, (_, product) in enumerate(featured_products.iterrows()):
    with featured_cols[index]:
        render_product_card(product, "featured")

st.divider()
heading_col, count_col = st.columns([4, 1], vertical_alignment="center")
with heading_col:
    st.markdown("<div class='section-heading'>Shop all products</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='section-caption'>{len(filtered)} products match your filters.</div>",
        unsafe_allow_html=True,
    )
with count_col:
    st.markdown(f"**{len(filtered)} results**")

active_filters = []
if search_query:
    active_filters.append(("Search", "search_query", search_query))
for value in selected_categories:
    active_filters.append((f"Category: {value}", "category_filter", value))
for value in selected_brands:
    active_filters.append((f"Brand: {value}", "brand_filter", value))
if price_range != filter_defaults["price_filter"]:
    active_filters.append((f"Price: {format_price_range(price_range)}", "price_filter", None))
if min_rating > 0:
    active_filters.append((f"Rating: {min_rating:g}+", "rating_filter", None))
for value in selected_colors:
    active_filters.append((f"Color: {value}", "color_filter", value))
if in_stock:
    active_filters.append(("In stock only", "stock_filter", None))
if min_discount:
    active_filters.append((f"Discount: {min_discount}%+", "discount_filter", None))

if active_filters:
    st.markdown("**Active filters**")
    filter_cols = st.columns(min(len(active_filters), 4), gap="small")
    for index, (label, state_key, value) in enumerate(active_filters):
        with filter_cols[index % len(filter_cols)]:
            if value is None:
                st.button(
                    f"{label}  ×",
                    key=f"remove_filter_{state_key}",
                    on_click=reset_filter,
                    args=(state_key,),
                    use_container_width=True,
                )
            else:
                st.button(
                    f"{label}  ×",
                    key=f"remove_filter_{state_key}_{value}",
                    on_click=(
                        reset_filter
                        if state_key == "search_query"
                        else remove_selected_value
                    ),
                    args=(state_key,) if state_key == "search_query" else (state_key, value),
                    use_container_width=True,
                )
    st.caption("Select a filter chip to remove it.")

if filtered.empty:
    st.warning("No products found. Try adjusting or clearing some filters.")
else:
    product_cols = st.columns(3, gap="medium")
    for index, (_, product) in enumerate(filtered.iterrows()):
        with product_cols[index % 3]:
            render_product_card(product, "results")

st.divider()
st.caption("Nexora · A better way to find the things you love.")
