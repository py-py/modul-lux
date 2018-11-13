let app = new Vue({
    el: '#app',
    delimiters: ['<%', '%>'],
    data: {
        modal: {
            name: null,
            pictures: [],
            description: null,
        }
    },
    methods: {
        openModalWindow: function (event) {
            console.log(this);
            console.log(event);
        },

    },

});
