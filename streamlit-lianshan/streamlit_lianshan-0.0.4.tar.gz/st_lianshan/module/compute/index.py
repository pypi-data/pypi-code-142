
# 定义单行选择表，选中行的数据，可以按字段/关键字读取出来
from st_aggrid_pro import GridOptionsBuilder, DataReturnMode, GridUpdateMode, AgGridPro


def aggrid(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    selection_mode = 'single'  # 定义单选模式，多选为'multiple'
    enable_enterprise_modules = True  # 设置企业化模型，可以筛选等
    gb.configure_default_column(editable=True, groupable=True)  # 定义允许编辑

    return_mode_value = DataReturnMode.FILTERED  # __members__[return_mode]
    gb.configure_selection(selection_mode, use_checkbox=True)  # 定义use_checkbox

    gb.configure_side_bar()
    # gb.configure_grid_options(domLayout='normal')
    # gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_pagination()
    gridOptions = gb.build()

    update_mode_value = GridUpdateMode.MODEL_CHANGED

    grid_response = AgGridPro(
        df,
        gridOptions=gridOptions,
        data_return_mode=return_mode_value,
        update_mode=update_mode_value,
        enable_enterprise_modules=enable_enterprise_modules,
        height=500,
    )
    df = grid_response['data']
    selected = grid_response['selected_rows']

    return df, selected
