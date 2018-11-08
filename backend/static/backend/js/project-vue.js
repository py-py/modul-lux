let app = new Vue({
    el: '#app',
    delimiters: ['<%', '%>'],
    data: {
        message: 'Hello Vue!',
        modal: {
            name: null,
            pictures: [],
            description: null,
        }
    },
    methods: {
        openModalView: function (event) {
            console.log(this);
            console.log(event);
        },

    },

});

$(document).on('opening', '.remodal', function () {
  console.log('Modal is opening');
});