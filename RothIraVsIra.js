function CompoundedValue(amount, rate, years){
  return amount * Math.pow((1 + rate),years);
}

function AmountAfterTaxes(amount, taxRate){
  return amount * ( 1 - taxRate );
}

function RothIraReturn(retirementContribution, growthRate, years, currentTaxRate){
  const amount = AmountAfterTaxes(retirementContribution, currentTaxRate);
  const compoundedValue = CompoundedValue(amount, growthRate, years);
  return compoundedValue;
}

function IraReturn(retirementContribution, growthRate, years, futureTaxRate){
  const compoundedValue = CompoundedValue(retirementContribution, growthRate, years);
  const retirementValue = AmountAfterTaxes(compoundedValue, futureTaxRate);
  return retirementValue;
}

function RothIraString(amount){
  return `Roth IRA Return ${amount}`;
}

function IraString(amount, futureVerb){
  return `IRA Future Tax Rate ${futureVerb} Return ${amount}`;
}

const retirementContribution = 100;
const growthRate = 0.06;
const years = 30;
const currentTaxRate = 0.30;
const futureTaxRateHigher = currentTaxRate + 0.05;
const futureTaxRateLower = currentTaxRate - 0.05;

const rothIra = RothIraReturn(retirementContribution, growthRate, years, currentTaxRate);
const iraFutureTaxRateLower = IraReturn(retirementContribution, growthRate, years, futureTaxRateLower);
const iraFutureTaxRateHigher = IraReturn(retirementContribution, growthRate, years, futureTaxRateHigher);

console.log(`${RothIraString(rothIra)}\n${IraString(iraFutureTaxRateHigher, 'higher')}\n${IraString(iraFutureTaxRateLower, 'lower')}`)
