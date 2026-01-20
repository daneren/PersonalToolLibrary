
# setting DEFALULT_COS_CONF_PATH
export DEFALULT_COS_CONF_PATH="~/.cos/ti_danerli_shanghai.conf"

# coscmd command
alias cdowns="coscmd -c $DEFALULT_COS_CONF_PATH download -rf "
alias cups="coscmd -c $DEFALULT_COS_CONF_PATH upload -rf "
alias cdown="coscmd -c $DEFALULT_COS_CONF_PATH download -f "
alias cup="coscmd -c $DEFALULT_COS_CONF_PATH upload -f "

