window.addEventListener("DOMContentLoaded", () => {
    const $ = id => document.getElementById(id);

    const numInput = $("numRecords");
    const decBtn = $("dec");
    const incBtn = $("inc");
    const localeEl = $("locale");
    const structEl = $("data-structure-textarea");
    const errorEl = $("error");
    const genBtn = $("generate");
    const clearBtn = $("clear");
    const outPre = $("output");
    const typesDiv = $("types");

    let supportedTypes = {};

    const clamp = (value, min, max) => Math.min(Math.max(Number(value), min), max);

    const autoResize = () => {
        structEl.style.height = "auto";
        structEl.style.height = `${structEl.scrollHeight}px`;
    };

    const transformToItalic = text =>
        text.replace(/'([^']+)'/g, '<b class="bold-text">$1</b>');

    const renderTypes = () => {
        typesDiv.innerHTML = "";

        for (const [category, types] of Object.entries(supportedTypes)) {
            const cdiv = document.createElement("div");
            cdiv.className = "supported-types-category";
            cdiv.innerHTML = `<h3 class="supported-types-category-title"><u>${category}</u></h3>`;

            const labels = document.createElement("div");
            labels.className = "supported-types-labels";

            for (const [name, info] of Object.entries(types)) {
                const item = document.createElement("div");
                item.className = "supported-types-item";

                const description = info.description
                    ? `<p class="supported-types-description">${transformToItalic(info.description)}</p>`
                    : "";

                const additional = info.additional?.length
                    ? `<ul class="supported-types-additional">${info.additional.map(i => `<li>${transformToItalic(i)}</li>`).join("")}</ul>`
                    : "";

                item.innerHTML = `
                    <label class="supported-types">- <i>${name}</i></label>
                    ${description}
                    ${additional}
                `;
                labels.appendChild(item);
            }

            cdiv.appendChild(labels);
            typesDiv.appendChild(cdiv);
        }
    };

    const fetchJSON = async (url) => {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`Failed to fetch ${url}`);
        return res.json();
    };

    const fetchInitialData = async () => {
        try {
            supportedTypes = await fetchJSON("/api/supported_types");
            renderTypes();

            const example = await fetchJSON("/api/exampleScheme");
            structEl.value = JSON.stringify(example, null, 4);
            autoResize();
        } catch (err) {
            console.error("Error during initial fetch:", err);
        }
    };

    const handleGenerate = async () => {
        try {
            const structure = JSON.parse(structEl.value);
            const payload = {
                structure,
                locale: localeEl.value,
                numRecords: Number(numInput.value)
            };

            const res = await fetch("/api/generate_data", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(payload)
            });

            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.error || "Server error");
            }

            const data = await res.json();
            outPre.textContent = JSON.stringify(data, null, 4);

            const blob = new Blob([JSON.stringify(data)], {type: "application/json"});
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "fake_data.json";
            link.click();
        } catch (err) {
            errorEl.textContent = err instanceof SyntaxError
                ? "Invalid JSON format. Please check your input."
                : err.message;
        }
    };

    // Event bindings
    structEl.addEventListener("input", () => {
        errorEl.textContent = "";
        autoResize();
    });

    structEl.addEventListener("keydown", (e) => {
        if (e.key === "Tab") {
            e.preventDefault();

            const start = structEl.selectionStart;
            const end = structEl.selectionEnd;
            const value = structEl.value;

            structEl.value = value.slice(0, start)
                + "\t"
                + value.slice(end);

            structEl.selectionStart = structEl.selectionEnd = start + 1;

            autoResize();
        }
    });

    genBtn.addEventListener("click", handleGenerate);

    clearBtn.addEventListener("click", () => {
        structEl.value = "{\n\t\n}";
        errorEl.textContent = "";
        autoResize();
    });

    decBtn.addEventListener("click", () => {
        numInput.value = clamp(numInput.value - 1, 1, 1000);
    });

    incBtn.addEventListener("click", () => {
        numInput.value = clamp(numInput.value + 1, 1, 1000);
    });

    const handleClampInput = () => {
        numInput.value = clamp(numInput.value, 1, 1000);
    };

    numInput.addEventListener("input", handleClampInput);
    numInput.addEventListener("blur", handleClampInput);

    numInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            handleClampInput();
            e.preventDefault();
            genBtn.click();
        }
    });

    fetchInitialData().then(r => {
    });
    autoResize();
});
