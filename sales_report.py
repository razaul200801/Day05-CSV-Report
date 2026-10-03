import csv

def read_sales_data(file_path):
    sales = []

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            customer = row['Customer']
            product = row['Product']
            quantity = int(row['Quantity'])
            unit_price = float(row['Unit Price'])

            total = quantity*unit_price

            sales.append({
               "Customer": customer,
                "Product": product,
                "Quantity": quantity,
                "Unit Price": unit_price,
                "Total": total
            })

            print(f"{customer} | {product} | Total: ${total:.2f}")

    return sales


def create_report(sales,file_path):
    # Create a summary of the sales data as Summary Report
    field_names = ["Customer", "Product", "Quantity", "Unit Price", "Total"]
    with open(file_path, mode = 'w', newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(sales)

    print(f"\nSummary report created at: {file_path}")


def show_summary(sales):

    total_revenue = sum(sale["Total"] for sale in sales)
    average_sale = total_revenue/len(sales)
    highest_sale = max(sales, key=lambda x: x["Total"])  # Return the sale as Dictionary with the highest total
    lowest_sale = min(sales, key=lambda x: x["Total"])

    print('\n--------- Sales Summary ----------')
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Average Sale: ${average_sale:.2f}")
    print(f"Highest Sale: ${highest_sale['Total']:.2f} ({highest_sale['Customer']} - {highest_sale['Product']})")
    print(f"Lowest Sale: ${lowest_sale['Total']:.2f} ({lowest_sale['Customer']} - {lowest_sale['Product']})")


def main():
    input_file = "sales_data.csv"
    output_file = "summary_report.csv"

    try:
        sales = read_sales_data(input_file)
        if not sales:
            print("No sales data found in the input file.")
            return
        
        create_report(sales, output_file)
        show_summary(sales)

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except ValueError as ve:
        print(f"Data format error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


#================================ Main Program Execution =================================
if __name__ == "__main__":
    main()