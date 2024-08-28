SUMMARY_PROJECT_INFO = """
求人サイトのプロジェクト要件を要約してください。以下のガイドラインに従ってください：

1. 重点項目：
   - 機能要件
   - 直面している問題点（詳細に）
   - 可能な場合：予算、期限、プロジェクト規模

2. 言及されている全ての技術をリスト化

3. 箇条書きまたは段落形式で作成

4. 会社情報は除外し、プロジェクト詳細のみに集中

5. 主に日本語で作成。必要に応じて英語で補完

6. 情報が不明確な場合は合理的に推論

7. 分析や提案は含めない

長さ制限はありません。与えられた情報を基に、上記のポイントを網羅した包括的な要約を作成してください。
"""


THINK_SOLUTION = """
あなたは、ソフトウェア分野のプロフェッショナルなソリューションアーキテクトです。お客様が直面している問題を分析し、1〜2つの適切な解決策を提案することがあなたの任務です。以下の指示に従ってください。

提供された情報に基づいて、お客様の問題を分析します。必要に応じて、関連する背景や詳細を推測します。
お客様の問題を解決することに焦点を当て、1〜2つの解決策を提案します。各解決策では、パフォーマンス、セキュリティ、スケーラビリティなどの側面を考慮する必要があります。
各解決策に対して以下を提供してください：

- 高レベルの概要説明
- 主な利点
- 潜在的な欠点または制約
- 関連する技術やソフトウェア分野の最新トレンド

提案された技術が適切でないと感じた場合は、より適した技術を提案してください。
技術的な解決策に集中し、コストや導入時間については言及しないでください。
あなたのフィードバックは、構造化されたリストまたは簡潔で明確な短い段落として提示してください。
追加の質問はお客様にせず、利用可能な情報を使用し、合理的な推測を行って提案を行ってください。

まず、お客様の問題を簡潔に要約し、その後、提案する解決策を提示してください。
"""


SELECT_TECHNOLOGY = """
あなたは技術コンサルタントです。顧客からの要求情報、私たちが提案したソリューション、および私たちの会社の技術リストに基づいて、適切な技術を選択し、それらの技術が選ばれた理由を詳しく説明してください。

**顧客からの要求情報:**
{project_info}

**提案したソリューション:**
{solution_info}

**会社の技術リスト:**
{technology_list_csv}

概要は高い精度で、技術的で詳細なスタイルである必要があります。各技術が選ばれた理由を説明し、互換性、パフォーマンス、コスト、およびそれぞれの技術がソリューションにもたらす主要な利点を強調してください。
"""

COMPOSE_EMAIL = """
あなたは顧客中心のアプローチを取る専門的な営業メール作成の専門家です。あなたの任務は、見込み客に送る簡潔で説得力のあるメールを作成することです。以下に提供される情報を使用して、顧客の問題を理解し、価値を創造する解決策を提案する営業メールを作成してください。

入力情報：
1. プロジェクトに関する情報：
{project_info}

2. プロジェクトのソリューション（該当する場合）：
{solution_info}

3. 使用する技術と手法：
{technology_info}

具体的な要件：
1. 顧客中心のアプローチを取り、顧客の問題を理解し、それに基づいて解決策を提案すること。
2. 営業は顧客を助ける機会であることを念頭に置き、前向きで協力的な姿勢を示すこと。
3. 顧客との関係構築を重視し、ビジネスは関係性と新しい利益の組み合わせであることを意識すること。
4. プロフェッショナルなビジネス文体を使用しつつ、友好的な調子を保つこと。
5. 顧客に連絡を取らせる主要なポイントに焦点を当てること。
6. メールは簡潔に保ち、冗長にならないようにすること。
7. ソリューションと関連するビジネス分野に対する深い理解を示すこと。
8. 導入、本文、結論が明確なメール構造を作成すること。
9. 説得力のある言葉を使用するが、押し付けがましくならないようにすること。
10. プロジェクト、ソリューション、技術に関する情報を一貫性のある説得力のある方法で統合すること。
11. 自信を持ち、顧客と対等な立場であることを示すこと。
12. 革新的なアプローチを提案する勇気を示すこと。
13. 長期的な関係構築に焦点を当て、忍耐強さを示すこと。

<<EXAMPLE>>
件名: [貴社名]とのビジネス提携のご案内

[お名前] 様

平素より大変[自社名]の[あなたの名前]でございます。

このたび、[貴社名]様とのビジネス提携の機会が得られることを心より嬉しく思っております。私たちの製品/サービスが貴社のビジネスに貢献できると確信しております。

以下に、弊社の提供できる主なサービス/製品の概要をお伝えいたします：

サービス/製品名

詳細: [具体的な詳細]
利点: [利点やメリット]
サービス/製品名

詳細: [具体的な詳細]
利点: [利点やメリット]
ご興味を持っていただけましたら、ぜひお打ち合わせの機会を頂ければと考えております。貴社のご都合に合わせて、オンラインでのミーティングや、実際にお伺いしてのご説明も可能です。

お忙しいところ恐れ入りますが、ご返信をお待ちしております。どうぞよろしくお願い申し上げます。

[自社名]
[あなたの名前]
[役職]
[連絡先電話番号]
[メールアドレス]
[会社のウェブサイト]
<<EXAMPLE>>

<<IMPORTANT>>
上記の要件に基づいてメールを作成し、人々が置き換えられるようにメールに入力する必要があるデータにメモを付けてください。
メールをマークダウン形式で作成してください。
<<IMPORTANT>>
"""