from dotenv import load_dotenv
import pandas as pd

load_dotenv()


class AIAgent:
    def __init__(self):
        self.llm = self._build_llm()

    def _build_llm(self):
        try:
            from langchain_openai import OpenAI
        except ImportError:
            return None
        return OpenAI(temperature=0)

    def process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.llm is None or df.empty:
            return df

        for start in range(0, len(df), 20):
            batch = df.iloc[start : start + 20]
            prompt = f"Clean the following data batch:\n{batch.to_csv(index=False)}"
            self.llm.invoke(prompt)
        return df
