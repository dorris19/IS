use v5.16;

use Lingua::EN::NamedEntity;
use Lingua::EN::Summarize;
use Data::Dumper;
my $text = qq{

Nevada's prisons pharmacy chief testified Wednesday that she obtained drugs for the lethal injection of a convicted killer despite knowing that drug manufacturers didn't want their products used for executions.

Department of Corrections Pharmacy Director Linda Fox said during questioning by attorneys representing drug companies that she made the online order of medications from a third-party supplier, Cardinal Health, and didn't specify the end use.
he acknowledged she later became alarmed when she learned that the manufacturer, Alvogen, had notified the state in writing that it didn't want its products used in executions.

Still, after communicating with prisons chief James Dzurenda, when another chance came a few days later, Fox bought more.

"Notwithstanding everything you knew coming into these three purchases about the industry, the publications, about the news, about the letters, the Department of Corrections ... honored none of those objections, is that right?" asked James Pisanelli, an attorney representing drug maker Alvogen.

"Yes," Fox said.

Alvogen, Hikma Pharmaceuticals USA and Sandoz Inc. are suing to stop the use of their products in Nevada's planned execution of inmate Scott Raymond Dozier.

They accuse prison officials of deceiving the public and the companies, and improperly obtaining Alvogen's sedative, Hikma's opioid fentanyl and a Sandoz paralyzing drug called cisatracurium for a use the companies say they don't allow.

Fentanyl, made by several companies, has been blamed for illegal use overdose deaths nationwide.

State attorneys say Nevada had no contract with the manufacturers, and the drug makers have no claim of product ownership.

Cardinal Health is not a defendant in the lawsuit, and company officials have declined requests for comment about the testimony this week before Clark County District Court Judge Elizabeth Gonzalez in Las Vegas.

Next week, the state Supreme Court is scheduled to hold hearings in Carson City on a separate bid by state attorneys to put Dozier's execution back on track for mid-November.

Fifteen states are siding with Nevada in that fight, led by Oklahoma and including Nebraska, where an inmate was put to death last month using a four-drug combination similar to the first-of-its-kind method Nevada developed last year.

The testimony before Gonzalez has provided a glimpse of a problem common to death-penalty states in the U.S.

Nevada got not one reply despite contacting nearly 250 drug companies and suppliers in 2016 with a straightforward request to supply medications for an execution, Dzurenda testified Tuesday.

After Cardinal posted the buyers' list that gave Fox a chance in May to obtain midazolam, Nevada rescheduled Dozier's execution for July.

Fox acknowledged Wednesday she thought it would look bad if the public learned that the purchase came just one day after the state Supreme Court heard arguments about Dozier's planned execution, which had been postponed last year.

"You said, "I'm sure from the outside it will look very contrived that I received the medication one day after we went to court," Pisanelli told Fox.

"You were also worried what you were going to look like, you and the state, weren't you?" he asked.

"Sure," Fox said.

};
my @entities = extract_entities($text);

print Dumper(@entities);
my $summary = summarize( $text );                    # Easy, no? :-)
my $summary = summarize( $text, maxlength => 500 );  # 500-byte summary
my $summary = summarize( $text, filter => 'html' );  # Strip HTML formatting
my $summary = summarize( $text, wrap => 75 );        # Wrap output to 75 col.
print $summary;
