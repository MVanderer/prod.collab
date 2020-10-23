module.exports = {
    presets: [
        [
            "@babel/env",
            {
                targets: {
                    /*edge: "17",
                    firefox: "60",
                    chrome: "67",
                    safari: "11.1"
                    esmodules: true,*/
                    ie: "11"
                },
                modules: "amd"
            }
        ]
    ],
    sourceType: "unambiguous"
};
