import pandas as pd
from helpers_task1.edmonds_karp import edmonds_karp

def generate_report(capacity_matrix: list, source_nodes: list, target_nodes: list) -> pd.DataFrame:
    report = []
    for source in source_nodes:
        for target in target_nodes:
            max_flow, flow_matrix = edmonds_karp(capacity_matrix, source, target)
            if max_flow > 0:  # Додаємо тільки реальні потоки
                # Додаємо у звіт
                report.append({
                    "Термінал": f"Термінал {source + 1}",
                    "Магазин": f"Магазин {target - len(source_nodes) - 3}",  # Магазини починаються після терміналів
                    "Фактичний Потік (одиниць)": max_flow
                })

    # Якщо звіт не порожній, створюємо DataFrame
    if report:
        report_df = pd.DataFrame(report)
    else:
        report_df = pd.DataFrame(columns=["Термінал", "Магазин", "Фактичний Потік (одиниць)"])

    return report_df