screen header():
    #hbox:
        #style "ratings"
        #add "ui/rating.png" 
    #label
    #hbox:
        #yalign 0.09
        #xalign 0.15
        #text "1000" color "#fff"
    hbox:
        box_wrap True
        style "currency"
        add "ui/f_currency.png" 
    #label
    hbox:
        yalign 0.09
        xalign 0.9
        text "[persistent.default_balance]" color "#fff"        

style ratings:
    yalign -0.1
    xalign 0.05

style currency:
    yalign -0.1
    xalign 0.95