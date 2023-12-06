import streamlit as st
import util

if __name__ == '__main__':
    ticker_symbol = st.sidebar.text_input(
    "Please enter the stock symbol", 'MSFT'
    )
    data_period = st.sidebar.text_input('Period', '10d')
    data_interval = st.sidebar.radio('Interval', ['15m','30m','1h','1d'])
    ema1 = st.sidebar.text_input('EMA 1', 20)
    ema2 = st.sidebar.text_input('EMA 2', 50)

    st.header("Strategi Investasi Saham Menggunakan Metode Moving Average Cross Over dengan Exponential Moving Average (EMA)")
    st.write("""
        - cross up (cyan) :point_right: BUY
        - cross down (magenta) :point_right: SELL
        ---
       ## Data Solusi 
    """)
    ticker_data = util.get_ticker_data(ticker_symbol, data_period, data_interval)

    if len(ticker_data) != 0:
        ticker_data = util.get_ema(ticker_data, int(ema1))
        ticker_data = util.get_ema(ticker_data, int(ema2))

        candle_fig = util.get_candle_chart(ticker_data)
        candle_fig = util.add_ema_trace(candle_fig, ticker_data.index, ticker_data['ema_' + ema1], 'EMA ' + ema1, "#ffeb3b")
        candle_fig = util.add_ema_trace(candle_fig, ticker_data.index, ticker_data['ema_' + ema2], 'EMA ' + ema2, "#2962ff")

        trades = util.create_ema_trade_list(ticker_data, 'ema_' + ema1, 'ema_' + ema2)
        ticker_data = util.join_trades_to_ticker_data(trades, ticker_data)
        candle_fig = util.add_trades_trace(candle_fig, ticker_data)
        
        trades
        st.write(candle_fig)