/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";


const QuoteButton = publicWidget.Widget.extend({

    selector: '#common_button',
    events: {
        click: '_onClick'
    },

    _onClick() {

        // TODO: Update Logic As per requirnment
        $('.o_newsletter_popup').removeClass('d-none')
        $('.s_popup_middle').removeClass('d-none').addClass('d-block').addClass('show');
    }

});

publicWidget.registry.quote_button = QuoteButton;

export default {
    QuoteButton: QuoteButton,
};
