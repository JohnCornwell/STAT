#############################################################################
# Generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#  Aug 03, 2022 04:49:56 AM CDT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m47" -background #000000 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1280x657+-8+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1284 701
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    set toptitle "STAT"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Window" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background #000000 -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.fra46" "SwarmFrame" vTcl:WidgetProc "Window" 1
    set site_3_0 $top.fra46
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -background #000000 -compound left -disabledforeground #a3a3a3 \
        -font {-family Arial -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Demand Details} 
    vTcl:DefineAlias "$site_3_0.lab50" "DemandDetailsLabel" vTcl:WidgetProc "Window" 1
    button $site_3_0.but53 \
        -activebackground white -activeforeground #000000 -background #f2b83d \
        -command PreviousTask -compound center -disabledforeground #a3a3a3 \
        -font {-family Arial -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Back 
    vTcl:DefineAlias "$site_3_0.but53" "BackButton" vTcl:WidgetProc "Window" 1
    button $site_3_0.but56 \
        -activebackground #f2b83d -activeforeground #000000 \
        -background #f2b83d -command nextTask -compound center \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Next 
    vTcl:DefineAlias "$site_3_0.but56" "NextButton" vTcl:WidgetProc "Window" 1
    label $site_3_0.lab61 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor nw -background #000000 -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 13 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Logged in as: } 
    vTcl:DefineAlias "$site_3_0.lab61" "UsernameLabel" vTcl:WidgetProc "Window" 1
    button $site_3_0.but62 \
        -activebackground #f2b83d -activeforeground #000000 \
        -background #f2b83d -command {Log Out} -compound center \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Log Out} 
    vTcl:DefineAlias "$site_3_0.but62" "LogOutButton" vTcl:WidgetProc "Window" 1
    label $site_3_0.lab109 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #000000 -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Task Demand Profile} 
    vTcl:DefineAlias "$site_3_0.lab109" "DemandProfileLabel" vTcl:WidgetProc "Window" 1
    ttk::combobox $site_3_0.tCo47 \
        \
        -values {square {positive sine} sine random cycloid {positive zig zag} {zig zag} stair trapezoid custom} \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo47" "DemandProfileEntry" vTcl:WidgetProc "Window" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #000000 -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Demand Amplitude} 
    vTcl:DefineAlias "$site_3_0.lab52" "DemandAmplitudeLabel" vTcl:WidgetProc "Window" 1
    entry $site_3_0.ent53 \
        -background #f2b83d -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 144 
    vTcl:DefineAlias "$site_3_0.ent53" "AmplitudeEntry" vTcl:WidgetProc "Window" 1
    label $site_3_0.lab59 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #000000 -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Demand Period} 
    vTcl:DefineAlias "$site_3_0.lab59" "DemandPeriodLabel" vTcl:WidgetProc "Window" 1
    entry $site_3_0.ent46 \
        -background #f2b83d -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 144 
    vTcl:DefineAlias "$site_3_0.ent46" "PeriodEntry" vTcl:WidgetProc "Window" 1
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #000000 -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text Range 
    vTcl:DefineAlias "$site_3_0.lab47" "RangeLabel" vTcl:WidgetProc "Window" 1
    entry $site_3_0.ent48 \
        -background #f2b83d -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 144 
    vTcl:DefineAlias "$site_3_0.ent48" "RangeEntry" vTcl:WidgetProc "Window" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #000000 -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family Arial -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f2b83d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Demand Function} 
    vTcl:DefineAlias "$site_3_0.lab49" "DemandFunctionLabel" vTcl:WidgetProc "Window" 1
    entry $site_3_0.ent50 \
        -background #f2b83d -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 234 
    vTcl:DefineAlias "$site_3_0.ent50" "FunctionEntry" vTcl:WidgetProc "Window" 1
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.41 -y 0 -rely 0.076 -width 0 \
        -relwidth 0.18 -height 0 -relheight 0.061 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -relx 0.523 -y 0 -rely 0.609 -width 107 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.406 -y 0 -rely 0.609 -width 107 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.68 -y 0 -rely 0.015 -width 0 \
        -relwidth 0.222 -height 0 -relheight 0.091 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but62 \
        -in $site_3_0 -x 0 -relx 0.906 -y 0 -rely 0.015 -width 107 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab109 \
        -in $site_3_0 -x 0 -relx 0.047 -y 0 -rely 0.304 -width 0 \
        -relwidth 0.15 -height 0 -relheight 0.032 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo47 \
        -in $site_3_0 -x 0 -relx 0.203 -y 0 -rely 0.304 -width 0 \
        -relwidth 0.113 -height 0 -relheight 0.032 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.359 -y 0 -rely 0.304 -width 0 \
        -relwidth 0.134 -height 0 -relheight 0.032 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent53 \
        -in $site_3_0 -x 0 -relx 0.523 -y 0 -rely 0.304 -width 144 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 0 -relx 0.672 -y 0 -rely 0.304 -width 0 \
        -relwidth 0.113 -height 0 -relheight 0.032 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 0 -relx 0.828 -y 0 -rely 0.304 -width 144 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.211 -y 0 -rely 0.472 -width 0 \
        -relwidth 0.048 -height 0 -relheight 0.032 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 0 -relx 0.289 -y 0 -rely 0.472 -width 144 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.477 -y 0 -rely 0.472 -width 0 \
        -relwidth 0.127 -height 0 -relheight 0.032 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent50 \
        -in $site_3_0 -x 0 -relx 0.617 -y 0 -rely 0.472 -width 234 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.fra46
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

