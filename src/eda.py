
# E-Commerce Sales, Customer and Profitability Analysis
# Complete Exploratory Data Analysis using Python.

import pandas as pd
import numpy as np

from data_loader import load_data


# ============================================================
# FUNCTION 1: BUSINESS PERFORMANCE KPIs
# ============================================================

def calculate_business_kpis(df):
    """
    Calculate overall business performance metrics.

    Metrics:
    Total Orders, Customers, Units, Sales, Cost, Profit,
    Average Order Value and Profit Margin.
    """

    total_orders = df["order_id"].nunique()
    total_customers = df["customer_id"].nunique()
    total_units = df["quantity"].sum()

    recorded_sales = df["sales_amount"].sum()
    total_cost = df["cost_amount"].sum()
    total_profit = df["profit"].sum()

    average_order_value = (
        recorded_sales / total_orders if total_orders else 0
    )

    profit_margin = (
        total_profit / recorded_sales * 100
        if recorded_sales else 0
    )

    return {
        "Total Orders": total_orders,
        "Total Customers": total_customers,
        "Total Units Sold": total_units,
        "Recorded Sales": round(recorded_sales, 2),
        "Total Cost": round(total_cost, 2),
        "Total Profit": round(total_profit, 2),
        "Average Order Value": round(average_order_value, 2),
        "Profit Margin (%)": round(profit_margin, 2)
    }


# ============================================================
# FUNCTION 2: MONTHLY SALES ANALYSIS
# ============================================================

def monthly_sales_analysis(df):
    """
    Analyze monthly sales, orders and profit.
    """

    valid_data = df.dropna(subset=["order_date"]).copy()

    valid_data["month"] = valid_data["order_date"].dt.month

    monthly_data = (
        valid_data.groupby("month")
        .agg(
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    return monthly_data.round(2)


# ============================================================
# FUNCTION 3: QUARTERLY SALES ANALYSIS
# ============================================================

def quarterly_sales_analysis(df):
    """
    Analyze quarterly sales and profitability.
    """

    valid_data = df.dropna(subset=["order_date"]).copy()

    valid_data["quarter"] = (
        valid_data["order_date"].dt.to_period("Q").astype(str)
    )

    quarterly_data = (
        valid_data.groupby("quarter")
        .agg(
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    return quarterly_data.round(2)


# ============================================================
# FUNCTION 4: CATEGORY PERFORMANCE ANALYSIS
# ============================================================

def category_performance_analysis(df):
    """
    Analyze sales and profitability across product categories.
    """

    category_data = (
        df.groupby("category")
        .agg(
            total_orders=("order_id", "nunique"),
            total_units=("quantity", "sum"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    category_data["profit_margin_pct"] = (
        category_data["total_profit"]
        / category_data["total_sales"] * 100
    )

    category_data = category_data.sort_values(
        "total_sales", ascending=False
    )

    return category_data.round(2)


# ============================================================
# FUNCTION 5: SUBCATEGORY PERFORMANCE ANALYSIS
# ============================================================

def subcategory_performance_analysis(df):
    """
    Analyze sales and profitability across subcategories.
    """

    subcategory_data = (
        df.groupby("sub_category")
        .agg(
            total_orders=("order_id", "nunique"),
            total_units=("quantity", "sum"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    subcategory_data["profit_margin_pct"] = (
        subcategory_data["total_profit"]
        / subcategory_data["total_sales"] * 100
    )

    subcategory_data = subcategory_data.sort_values(
        "total_sales", ascending=False
    )

    return subcategory_data.round(2)


# ============================================================
# FUNCTION 6: TOP 5 PRODUCT ANALYSIS
# ============================================================

def top_products_analysis(df):
    """
    Identify the top five products based on total sales.
    """

    top_products = (
        df.groupby(["product_id", "product_name", "category"])
        .agg(
            total_orders=("order_id", "nunique"),
            total_units=("quantity", "sum"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
        .head(5)
    )

    top_products["profit_margin_pct"] = (
        top_products["total_profit"]
        / top_products["total_sales"] * 100
    )

    return top_products.round(2)


# ============================================================
# FUNCTION 7: CUSTOMER BEHAVIOUR ANALYSIS
# ============================================================

def customer_behavior_analysis(df):
    """
    Classify customers as One-Time or Repeat customers.

    Classification is based on unique order frequency.
    """

    customer_orders = (
        df.groupby("customer_id")
        .agg(
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    customer_orders["customer_type"] = np.where(
        customer_orders["total_orders"] > 1,
        "Repeat Customer",
        "One-Time Customer"
    )

    customer_analysis = (
        customer_orders.groupby("customer_type")
        .agg(
            total_customers=("customer_id", "nunique"),
            total_orders=("total_orders", "sum"),
            total_sales=("total_sales", "sum"),
            total_profit=("total_profit", "sum")
        )
        .reset_index()
    )

    total_sales = customer_analysis["total_sales"].sum()

    customer_analysis["sales_contribution_pct"] = (
        customer_analysis["total_sales"] / total_sales * 100
        if total_sales else 0
    )

    return customer_analysis.round(2)


# ============================================================
# FUNCTION 8: CUSTOMER SEGMENT ANALYSIS
# ============================================================

def customer_segment_analysis(df):
    """
    Analyze New, Returning and Loyalty customer segments.

    Uses the existing customer_segment column.
    """

    segment_data = (
        df.groupby("customer_segment")
        .agg(
            total_customers=("customer_id", "nunique"),
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
    )

    segment_data["profit_margin_pct"] = (
        segment_data["total_profit"]
        / segment_data["total_sales"] * 100
    )

    return segment_data.round(2)


# ============================================================
# FUNCTION 9: GENDER-WISE CUSTOMER ANALYSIS
# ============================================================

def gender_analysis(df):
    """
    Analyze customer sales and profit by gender.
    """

    gender_data = (
        df.groupby("gender")
        .agg(
            total_customers=("customer_id", "nunique"),
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
    )

    gender_data["profit_margin_pct"] = (
        gender_data["total_profit"]
        / gender_data["total_sales"] * 100
    )

    return gender_data.round(2)


# ============================================================
# FUNCTION 10: AGE GROUP ANALYSIS
# ============================================================

def age_group_analysis(df):
    """
    Analyze customer behaviour across different age groups.
    """

    age_data = df.copy()

    age_data["age_group"] = pd.cut(
        age_data["age"],
        bins=[17, 25, 35, 45, 55, 65],
        labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
    )

    age_analysis = (
        age_data.dropna(subset=["age_group"])
        .groupby("age_group", observed=True)
        .agg(
            total_customers=("customer_id", "nunique"),
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    age_analysis["profit_margin_pct"] = (
        age_analysis["total_profit"]
        / age_analysis["total_sales"] * 100
    )

    return age_analysis.round(2)


# ============================================================
# FUNCTION 11: STATE-WISE SALES ANALYSIS
# ============================================================

def state_analysis(df):
    """
    Analyze sales and profitability across Indian states.
    """

    state_data = (
        df.groupby("state")
        .agg(
            total_customers=("customer_id", "nunique"),
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
    )

    state_data["profit_margin_pct"] = (
        state_data["total_profit"]
        / state_data["total_sales"] * 100
    )

    return state_data.round(2)


# ============================================================
# FUNCTION 12: CITY-WISE SALES ANALYSIS
# ============================================================

def city_analysis(df):
    """
    Analyze sales and profitability across cities.
    """

    city_data = (
        df.groupby("city")
        .agg(
            total_customers=("customer_id", "nunique"),
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
    )

    city_data["profit_margin_pct"] = (
        city_data["total_profit"]
        / city_data["total_sales"] * 100
    )

    return city_data.round(2)


# ============================================================
# FUNCTION 13: PAYMENT METHOD ANALYSIS
# ============================================================

def payment_method_analysis(df):
    """
    Analyze orders, customers and profitability by payment method.
    """

    payment_data = (
        df.groupby("payment_method")
        .agg(
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
    )

    payment_data["profit_margin_pct"] = (
        payment_data["total_profit"]
        / payment_data["total_sales"] * 100
    )

    return payment_data.round(2)


# ============================================================
# FUNCTION 14: SALES CHANNEL ANALYSIS
# ============================================================

def sales_channel_analysis(df):
    """
    Analyze sales and profitability across sales channels.
    """

    channel_data = (
        df.groupby("sales_channel")
        .agg(
            total_orders=("order_id", "nunique"),
            total_customers=("customer_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
        .sort_values("total_sales", ascending=False)
    )

    channel_data["profit_margin_pct"] = (
        channel_data["total_profit"]
        / channel_data["total_sales"] * 100
    )

    return channel_data.round(2)


# ============================================================
# FUNCTION 15: ORDER STATUS ANALYSIS
# ============================================================

def order_status_analysis(df):
    """
    Analyze order distribution and financial performance by status.

    Sales and profit are recorded values. Cancelled and returned
    orders should not automatically be treated as realized revenue.
    """

    status_data = (
        df.groupby("order_status")
        .agg(
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    total_orders = status_data["total_orders"].sum()

    status_data["order_percentage"] = (
        status_data["total_orders"] / total_orders * 100
        if total_orders else 0
    )

    status_data["profit_margin_pct"] = (
        status_data["total_profit"]
        / status_data["total_sales"] * 100
    )

    status_data = status_data.sort_values(
        "total_orders", ascending=False
    )

    return status_data.round(2)


# ============================================================
# FUNCTION 16: DISCOUNT ANALYSIS
# ============================================================

def discount_analysis(df):
    """
    Analyze discount groups and their relationship with profit margin.
    """

    discount_data = df.copy()

    discount_data["discount_group"] = pd.cut(
        discount_data["discount_pct"],
        bins=[-0.01, 5, 10, 15, 20, 25],
        labels=["0-5%", "5-10%", "10-15%", "15-20%", "20-25%"],
        include_lowest=True
    )

    discount_summary = (
        discount_data.dropna(subset=["discount_group"])
        .groupby("discount_group", observed=True)
        .agg(
            total_orders=("order_id", "nunique"),
            total_sales=("sales_amount", "sum"),
            total_profit=("profit", "sum"),
            average_discount=("discount_pct", "mean")
        )
        .reset_index()
    )

    discount_summary["profit_margin_pct"] = (
        discount_summary["total_profit"]
        / discount_summary["total_sales"] * 100
    )

    return discount_summary.round(2)


# ============================================================
# FUNCTION 17: DELIVERY PERFORMANCE ANALYSIS
# ============================================================

def delivery_performance_analysis(df):
    """
    Analyze delivery time and average product ratings.

    Only Delivered orders are included.
    """

    delivered_data = (
        df[df["order_status"] == "Delivered"]
        .dropna(subset=["delivery_days"])
    )

    delivery_data = (
        delivered_data.groupby("delivery_days")
        .agg(
            total_orders=("order_id", "nunique"),
            average_rating=("product_rating", "mean"),
            total_sales=("sales_amount", "sum")
        )
        .reset_index()
        .sort_values("delivery_days")
    )

    return delivery_data.round(2)


# ============================================================
# FUNCTION 18: CORRELATION ANALYSIS
# ============================================================

def correlation_analysis(df):
    """
    Calculate correlations between numerical business variables.
    """

    numeric_columns = [
        "age",
        "quantity",
        "unit_price",
        "discount_pct",
        "shipping_fee",
        "sales_amount",
        "cost_amount",
        "profit",
        "delivery_days",
        "product_rating"
    ]

    correlation_matrix = df[numeric_columns].corr()

    return correlation_matrix.round(2)


# ============================================================
# FUNCTION 19: LOSS ANALYSIS
# ============================================================

def loss_analysis(df):
    """
    Identify loss-making orders and analyze losses by category
    and product.

    Negative profit is treated as a business loss.
    """

    loss_orders = df[df["profit"] < 0].copy()

    # Calculate overall loss summary.
    total_loss_orders = loss_orders["order_id"].nunique()
    total_loss_amount = abs(loss_orders["profit"].sum())

    loss_summary = {
        "Loss-Making Orders": total_loss_orders,
        "Total Loss Amount": round(total_loss_amount, 2)
    }

    # Calculate losses by product category.
    category_loss = (
        loss_orders.groupby("category")
        .agg(
            loss_orders=("order_id", "nunique"),
            total_loss=("profit", "sum")
        )
        .reset_index()
    )

    category_loss["total_loss"] = category_loss["total_loss"].abs()

    category_loss = category_loss.sort_values(
        "total_loss", ascending=False
    )

    # Calculate losses by product.
    product_loss = (
        loss_orders.groupby(["product_id", "product_name", "category"])
        .agg(
            loss_orders=("order_id", "nunique"),
            total_loss=("profit", "sum")
        )
        .reset_index()
    )

    product_loss["total_loss"] = product_loss["total_loss"].abs()

    product_loss = product_loss.sort_values(
        "total_loss", ascending=False
    )

    return loss_summary, category_loss.round(2), product_loss.round(2)


# ============================================================
# MAIN PROGRAM: RUN ALL ANALYSIS FUNCTIONS
# ============================================================

if __name__ == "__main__":

    # Load the cleaned dataset.
    df = load_data()

    print("\n" + "=" * 65)
    print("             E-COMMERCE SALES ANALYSIS")
    print("=" * 65)

    # --------------------------------------------------------
    # 1. BUSINESS PERFORMANCE KPIs
    # --------------------------------------------------------

    print("\n1. BUSINESS PERFORMANCE KPIs")
    print("-" * 65)

    kpis = calculate_business_kpis(df)

    for metric, value in kpis.items():
        print(f"{metric}: {value}")

    # --------------------------------------------------------
    # 2. MONTHLY SALES ANALYSIS
    # --------------------------------------------------------

    print("\n2. MONTHLY SALES ANALYSIS")
    print("-" * 65)

    print(monthly_sales_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 3. QUARTERLY SALES ANALYSIS
    # --------------------------------------------------------

    print("\n3. QUARTERLY SALES ANALYSIS")
    print("-" * 65)

    print(quarterly_sales_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 4. CATEGORY PERFORMANCE
    # --------------------------------------------------------

    print("\n4. CATEGORY PERFORMANCE ANALYSIS")
    print("-" * 65)

    print(category_performance_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 5. SUBCATEGORY PERFORMANCE
    # --------------------------------------------------------

    print("\n5. SUBCATEGORY PERFORMANCE ANALYSIS")
    print("-" * 65)

    print(subcategory_performance_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 6. TOP 5 PRODUCTS
    # --------------------------------------------------------

    print("\n6. TOP 5 PRODUCTS ANALYSIS")
    print("-" * 65)

    print(top_products_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 7. CUSTOMER BEHAVIOUR
    # --------------------------------------------------------

    print("\n7. CUSTOMER BEHAVIOUR ANALYSIS")
    print("-" * 65)

    print(customer_behavior_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 8. CUSTOMER SEGMENT
    # --------------------------------------------------------

    print("\n8. CUSTOMER SEGMENT ANALYSIS")
    print("-" * 65)

    print(customer_segment_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 9. GENDER ANALYSIS
    # --------------------------------------------------------

    print("\n9. GENDER-WISE ANALYSIS")
    print("-" * 65)

    print(gender_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 10. AGE GROUP ANALYSIS
    # --------------------------------------------------------

    print("\n10. AGE GROUP ANALYSIS")
    print("-" * 65)

    print(age_group_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 11. STATE ANALYSIS
    # --------------------------------------------------------

    print("\n11. STATE-WISE ANALYSIS")
    print("-" * 65)

    print(state_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 12. CITY ANALYSIS
    # --------------------------------------------------------

    print("\n12. CITY-WISE ANALYSIS")
    print("-" * 65)

    print(city_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 13. PAYMENT METHOD ANALYSIS
    # --------------------------------------------------------

    print("\n13. PAYMENT METHOD ANALYSIS")
    print("-" * 65)

    print(payment_method_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 14. SALES CHANNEL ANALYSIS
    # --------------------------------------------------------

    print("\n14. SALES CHANNEL ANALYSIS")
    print("-" * 65)

    print(sales_channel_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 15. ORDER STATUS ANALYSIS
    # --------------------------------------------------------

    print("\n15. ORDER STATUS ANALYSIS")
    print("-" * 65)

    print(order_status_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 16. DISCOUNT ANALYSIS
    # --------------------------------------------------------

    print("\n16. DISCOUNT ANALYSIS")
    print("-" * 65)

    print(discount_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 17. DELIVERY PERFORMANCE
    # --------------------------------------------------------

    print("\n17. DELIVERY PERFORMANCE ANALYSIS")
    print("-" * 65)

    print(delivery_performance_analysis(df).to_string(index=False))

    # --------------------------------------------------------
    # 18. CORRELATION ANALYSIS
    # --------------------------------------------------------

    print("\n18. CORRELATION ANALYSIS")
    print("-" * 65)

    print(correlation_analysis(df).to_string())

    # --------------------------------------------------------
    # 19. LOSS ANALYSIS
    # --------------------------------------------------------

    print("\n19. LOSS ANALYSIS")
    print("-" * 65)

    loss_summary, category_loss, product_loss = loss_analysis(df)

    for metric, value in loss_summary.items():
        print(f"{metric}: {value}")

    print("\nCategory-wise Loss:")
    print(category_loss.to_string(index=False))

    print("\nTop 10 Loss-Making Products:")
    print(product_loss.head(10).to_string(index=False))

    # --------------------------------------------------------
    # FINAL MESSAGE
    # --------------------------------------------------------

    print("\n" + "=" * 65)
    print("          ALL ANALYSES COMPLETED SUCCESSFULLY")
    print("=" * 65)
