import asyncio


async def data_validation_orchestrator(financial_strengths,
                                       growth_rank,
                                       liquidity_ratio,
                                       profitability_rank,
                                       gf_value_rank):
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(varify_cash_to_debt_ratio(financial_strengths)),
            tg.create_task(verify_debt_to_equity_ratio(financial_strengths)),
            tg.create_task(verify_debt_to_ebitda_ratio(financial_strengths)),
            tg.create_task(verify_interest_coverage_ratio(financial_strengths)),
            tg.create_task(verify_roe(profitability_rank)),
            tg.create_task(verify_roa(profitability_rank)),
            tg.create_task(verify_roic(profitability_rank)),
            tg.create_task(verify_price_to_earnings_ratio(gf_value_rank, growth_rank)),
            tg.create_task(verify_peg_ratio(gf_value_rank)),
            tg.create_task(verify_price_to_sales_ratio(gf_value_rank)),
            tg.create_task(verify_price_to_book_ratio(gf_value_rank)),
            tg.create_task(verify_price_to_free_cash_flow_ratio(gf_value_rank))
        ]

    if all(tasks):
        return True


async def varify_cash_to_debt_ratio(data):
    if data['Cash-To-Debt'] > 0.20:
        return True

async def verify_debt_to_equity_ratio(data):
    if data['Debt-to-Equity'] < 1:
        return True

async def verify_debt_to_ebitda_ratio(data):
    if data['Debt-to-EBITDA'] < 2.5:
        return True

async def verify_interest_coverage_ratio(data):
    if data['Interest Coverage'] > 5:
        return True

async def verify_roe(data):
    if data['ROE %'] > 12:
        return True

async def verify_roa(data):
    if data['ROA %'] > 5:
        return True

async def verify_roic(data):
    if data['ROIC %'] > 12:
        return True


async def verify_price_to_earnings_ratio(gf_data,growth_rank_data):
    revenue = growth_rank_data['3-Year Revenue Growth Rate'] if not None else 0
    pe = gf_data['PE Ratio']

    if revenue == 0 and pe <11:
        return True

    if revenue in range(5,8) and pe < 17:
        return True

    if revenue in range(10,13) and pe <25:
        return True


async def verify_peg_ratio(data):
    if data['PEG Ratio'] <1:
        return True

async def verify_price_to_sales_ratio(data):
    if data['PS Ratio'] < 2:
        return True

async def verify_price_to_book_ratio(data):
    if data['PB Ratio'] <3:
        return True


async def verify_price_to_free_cash_flow_ratio(data):
    if data['Price-to-Free-Cash-Flow'] < 25:
        return True