export const Web = {
    getData() {
        return [
            {
                "website": "vuejs.org",
                "reason": "JS Framework for easier coding"
            },
            {
                "website": "primevue.org",
                "reason": "For the components and UI theming"
            },
            {
                "website": "generatedata.com",
                "reason": "For generating user data in tables"
            },
            {
                "website": "www.magicpattern.design/tools/css-backgrounds",
                "reason": "For generating the CSS background patterns"
            },
            {
                "website": "iconscout.com",
                "reason": "For the 3d images"
            }
            ]
    },
    getWebs() {
        return Promise.resolve(this.getData());
    },};