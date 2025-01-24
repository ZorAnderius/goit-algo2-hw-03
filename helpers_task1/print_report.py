import pandas as pd

def print_flow_report(report_df: pd.DataFrame):
    if report_df.empty:
        print("Немає потоку між терміналами та магазинами.")
    else:
        print(report_df.to_string(index=False))