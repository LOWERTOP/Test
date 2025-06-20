// Spotify Feature Toggle Script (independent, only affects tab/useractivity)

function parseArguments() {
    const defaultArgs = {
        tab: true,
        useractivity: false
    };
    try {
        if (typeof $argument === 'string') {
            return Object.assign(defaultArgs, JSON.parse($argument));
        } else if (typeof $argument === 'object') {
            return Object.assign(defaultArgs, $argument);
        } else {
            return defaultArgs;
        }
    } catch (e) {
        return defaultArgs;
    }
}

function patchAssignedValues(configuration, args) {
    if (!configuration || !configuration.assignedValues) return;
    for (let i of configuration.assignedValues) {
        const { name, scope } = i.propertyId || {};

        if (args.tab && name === "tab_configuration" && scope === "ios-feature-navigation") {
            if (i.enumValue && typeof i.enumValue.value === "string") {
                i.enumValue.value = "";
            }
        }

        if (!args.useractivity && name === "is_useractivity_sharing_enabled" && scope === "ios-feature-share") {
            if (i.boolValue && typeof i.boolValue.value === "boolean") {
                i.boolValue.value = false;
            }
        }
    }
}

try {
    const args = parseArguments();
    const body = JSON.parse($response.body);
    const config = body?.ucsResponseV0?.success?.resolveSuccess?.configuration;

    patchAssignedValues(config, args);

    $done({ body: JSON.stringify(body) });
} catch (e) {
    console.log("[SpotifyFeatureToggle] Error:", e);
    $done({});
}
