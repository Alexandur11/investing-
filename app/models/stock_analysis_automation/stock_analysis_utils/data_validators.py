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

    results = await asyncio.gather(*tasks, return_exceptions=True)
    if all(results):
        return True


async def varify_cash_to_debt_ratio(data):
    try:
        if data['cash_to_debt'] > 0.20:
            return True
    except Exception as e:
        print(f'Error obtaining cash to debt: {e}')

async def verify_debt_to_equity_ratio(data):
    try:
        if data['debt_to_equity'] < 1:
            return True
    except Exception as e:
        print(f'Error obtaining debt to equity: {e}')

async def verify_debt_to_ebitda_ratio(data):
    try:
        if data['debt_to_ebitda'] < 2.5:
            return True
    except Exception as e:
        print(f'Error obtaining ebitda: {e}')

async def verify_interest_coverage_ratio(data):
    try:
        if data['interest_coverage_ratio'] < 5:
            return False
    except Exception as e:
        print(f'Error obtaining interest coverage: {e}')

    return True

async def verify_current_ratio(data):
    try:
        if data['current_ratio'] < 1:
            return True
    except Exception as e:
        print(f'Error obtaining current ratio: {e}')
async def verify_roe(data):
    try:
        if data['roe'] > 12:
            return True
    except Exception as e:
        print(f'Error obtaining roe: {e}')

async def verify_roa(data):
    try:
        if data['roa'] > 5:
            return True
    except Exception as e:
        print(f'Error obtaining roa: {e}')

async def verify_roic(data):
    try:
        if data['roic'] > 12:
            return True
    except Exception as e:
        print(f'Error obtaining roic {e}')


async def verify_price_to_earnings_ratio(gf_data,growth_rank_data):
    try:
        revenue = growth_rank_data['3-Year Revenue Growth Rate'] if not None else 0
        pe = gf_data['P/E Ratio']

        if revenue == 0 and pe <11:
            return True

        if revenue in range(5,8) and pe < 17:
            return True

        if revenue in range(10,13) and pe <25:
            return True
    except Exception as e:
        print(f'Error obtaining P/E: {e}')


async def verify_peg_ratio(data):
    try:
        if data['PEG Ratio'] <1:
            return True
    except Exception as e:
        print(f'Error obtaining peg: {e}')

async def verify_price_to_sales_ratio(data):
    try:
        if data['PS Ratio'] < 2:
            return True
    except Exception as e:
        print(f'Error obtaining P/S: {e}')

async def verify_price_to_book_ratio(data):
    try:
        if data['PB Ratio'] <3:
            return True
    except Exception as e:
        print(f'Error obtaining P/B: {e}')

async def verify_price_to_free_cash_flow_ratio(data):
    try:
        if data['P FCF'] < 25:
            return True
    except Exception as e:
        print(f'Error obtaining P/FCF: {e}')