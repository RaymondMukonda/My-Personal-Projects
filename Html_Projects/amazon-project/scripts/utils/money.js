export function formatCurrency(priceCents) {
    return (Math.round(priceCents) / 100).toFixed(2);
}

// Each file can only have 1 default export, us only if you expoting one thing from the line to have clean code
// example ( import formatCurrency from './utils/money.js'; ) in your checkout file 
export default formatCurrency;